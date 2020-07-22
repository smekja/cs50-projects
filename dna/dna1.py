import csv, cs50, sys

str = []
string = ""
dna_list = []
dna_temp = ""
y_list = []

try:
    with open(sys.argv[1],"r", newline =None) as STR_table:
        first_line = STR_table.readline()

    with open(sys.argv[2],"r") as dna_seq:
        dna = dna_seq.read()
        print(dna)
except:
    print("Usage: python dna.py data.csv sequence.txt")

#stripping newline
first_line = first_line.rstrip()
first_line += ","
#lenght of dna
dna_len = len(dna)

# making a list of STR
for char in first_line:
            if "," not in char:
                string = string + char
            if "," == char:
                str.append(string)
                string = ""
str.remove("name")
print(str)

# checking for each STR in DNA sequence and saving the result in y_list
for item in str:
    y = 0
    substring = item
    substring_len = len(substring)
    # making a list from every position of length of substring
    for i in range(dna_len):
        # reseting the list
        stop = 0
        x = 0
        while stop < dna_len:
            dna_temp = ""
            dna_temp = dna[i + stop:i + substring_len + stop]
            #checking how many times is substring after each other in the dna
            if dna_temp != substring:
                x = 0
                stop = stop + substring_len
                break

            if dna_temp == substring:
                x = x + 1
            if x > y:
                y = x
            stop = stop + substring_len




        #print(i)
    y_list.append(y)

print (y_list)
# print(substring_len)
# print(dna[0:substring_len])
