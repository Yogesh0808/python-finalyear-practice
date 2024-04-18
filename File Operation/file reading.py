import os 

fileloc = "/Users/yogesh/Projects/Final-Year-Python/File Operation/demo.txt"

with open(fileloc, 'r') as file:
    line = file.readline()
    while line != "":
        print(line)
        line = file.readline()
    