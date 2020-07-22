import csv, cs50, sys

str = []
string = ""
dna_list = []
dna_temp = ""
y_list = []

# Opening files for initial read
try:
    with open(sys.argv[1],"r", newline =None) as STR_table:
        first_line = STR_table.readline()

    with open(sys.argv[2],"r") as dna_seq:
        dna = dna_seq.read()
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

# checking for one STR pattern in the whole dna
def check_dna(substring_len, substring):
    y = 0
    for i in range(dna_len):
            stop = 0
            x = 0
            while stop < dna_len:
                dna_temp = ""
                dna_temp = dna[i + stop:i + substring_len + stop]
                #checking how many times is substring after each other in the dna
                if dna_temp != substring:
                    x = 0
                    break

                if dna_temp == substring:
                    x = x + 1
                if x > y:
                    y = x
                stop = stop + substring_len
    return y


# checking for each STR in DNA sequence and saving the result in y_list
for item in str:
    substring = item
    substring_len = len(substring)
    # making a list from every position of length of substring
    y = check_dna(substring_len, substring)
    y_list.append(y)

# comparing STR found in the dna with suspects
with open(sys.argv[1],"r", newline =None) as STR_table:
    x = 0
    suspect = 0
    for line in STR_table:
        if x == 0:
            x = 1
            continue
        new_line = line.strip()
        new_line = new_line.split(",")
        length = len(new_line)
        check = 0
        for i in range(1, length):
            if int(new_line[i]) == y_list[i-1]:
                check = check + 1
        if check == length - 1:
            suspect = new_line[0]
    if suspect == 0:
        print("No match")
    else:
        print(suspect)

