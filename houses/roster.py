from cs50 import SQL
import sys
import csv

db = SQL("sqlite:///students.db")

# Checking for correct usage of command line arguments
if len(sys.argv) != 2:
    print("Error: Incorrect number of command line arguments. Usage: python roster.py Gryffindor")
    quit()
house = sys.argv[1]

# Selecting only the house we are looking for
list = db.execute("SELECT first, middle, last, birth FROM students WHERE house = (?) ORDER BY last, first;",
    house)

# Printing the names of people in the house
for row in list:
    first = row["first"]
    middle = row["middle"]
    if middle == None:
        middle = ""
    last = row["last"]
    birth = row["birth"]
    if middle == "":
        print(first," ", middle, last,", born"," ",birth, sep="")
    else:
        print(first," ", middle," ", last,", born"," ",birth, sep="")
