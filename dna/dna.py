# dna.py created for cs50 2020
import csv
from sys import argv, exit

# check for arguments
if len(argv) != 3:
    print("Missing command line arguments")
    exit(1)

# open dna file
dnaFile = open(argv[2], 'r')
dnaReader = csv.reader(dnaFile)
for row in dnaReader:
    dnaData = row

STR = dnaData[0]    # just to count length

# create new dictto store sequences
seqData = dict()

# open dna sequences

seqFile = open(argv[1])
people = csv.reader(seqFile)
for row in people:
    dnaSeq = row
    dnaSeq.pop(0)
    break

for item in dnaSeq:
    seqData[item] = 1

# iterate to count STRs
for key in seqData:
    n = len(key)
    tempMax = 0
    temp = 0
    for i in range(len(STR)):
        while temp > 0:
            temp -= 1
            continue

        if STR[i: i + n] == key:
            while STR[i - n: i] == STR[i: i + n]:
                temp += 1
                i += n

            if temp > tempMax:
                # store the maximum number of iteration
                tempMax = temp

    seqData[key] += tempMax

# compare data
# open file and store in dict for comparing
seqFile = open(argv[1])
people = csv.DictReader(seqFile)
for person in people:
    match = 0
    for STR in seqData:
        if seqData[STR] == int(person[STR]):
            match += 1
        if match == len(seqData):
            print(person['name'])
            exit(0)

# print if STR not found
print("No match")
