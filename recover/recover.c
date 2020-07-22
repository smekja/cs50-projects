#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

int jpeg_count = 0;
char filename[8];
int found = 0;
FILE *img = 0;
int end = 0;

int main(int argc, char *argv[])
{
    // Checking for correct command line argument
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover image\n");
        return 1;
    }

    // Opening memory card file
    FILE *mprt = fopen(argv[1], "r");
    // Checking if the return value is 0 - error
    if (mprt == NULL)
    {
        fprintf(stderr, "Couldn't open the file.\n");
    }

    uint8_t block[512];

    // Running until reaching the end of the file
    while (fread(block, 1, 512, mprt) == 512)
    {
        // Checking for beginning of a JPEG
        if (block[0] == 0xff && block[1] == 0xd8 && block[2] == 0xff && (block[3] & 0xf0) == 0xe0)
        {
            if (jpeg_count == 0)
            {
                // Changing the name of the new file based on how many files we already have
                sprintf(filename, "%03i.jpg", jpeg_count);

                // Opening a new JPEG file
                img = fopen(filename, "w");
                jpeg_count++;

                //Writing 512 B blocks to the JPEG file
                fwrite(block, 1, 512, img);
            }

            else
            {
                // Closing the current JPEG file
                fclose(img);

                // Changing the name of the new file based on how many files we already have
                sprintf(filename, "%03i.jpg", jpeg_count);

                // Opening a new JPEG file
                img = fopen(filename, "w");
                jpeg_count++;

                //Writing 512 B blocks to the JPEG file
                fwrite(block, 1, 512, img);
            }
            found = 1;

        }

        else if (found == 1)
        {
            //Writing 512 B block to the JPEG file
            fwrite(block, 1, 512, img);
        }
    }
    fclose(img);

}
