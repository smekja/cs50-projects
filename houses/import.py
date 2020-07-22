from cs50 import SQL
import sys
import csv

db = SQL("sqlite:///students.db")

# Checking for correct usage of command line arguments
if len(sys.argv) != 2:
    print("Error: Incorrect number of command line arguments. Usage: python import.py file.csv")
    quit()


# Opening csv file for reading
with open(sys.argv[1],"r", newline =None) as characters:
    # Create DictReader
    reader = csv.DictReader(characters, delimiter = ",")

    for row in reader:
        name = row["name"]
        house = row["house"]
        birth = int(row["birth"])
        name_list = name.split()
        list_len = len(name_list)
        # Checking for middle name and splitting the name up into first, middle and last
        if list_len == 2:
            first = name_list[0]
            middle = None
            last = name_list[1]
        else:
            first = name_list[0]
            middle = name_list[1]
            last = name_list[2]

        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)",
            first, middle, last, house, birth)


