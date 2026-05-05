# Chapter 6, Programming Exercise #2 
# Module 8—Exercise 1—Solution file—Your Name

import csv

# Global Declarations to match Pseudocode
geraldineFile = None
gerardFile = None
mergedFile = None

geraldineNum = 0
geraldineLastName = ""
geraldineAddress = ""
geraldineArea = 0

gerardNum = 0
gerardLastName = ""
gerardAddress = ""
gerardArea = 0

areBothAtEnd = "N"
END_NUM = 999

# Iterators to simulate reading lines from a file
geraldineReader = None
gerardReader = None
mergedWriter = None

def getReady():
    global geraldineFile, gerardFile, mergedFile
    global geraldineReader, gerardReader, mergedWriter
    
    # Opening files
    # Using .csv as per original sample data provided
    geraldineFile = open("Geraldines Businesses.csv", "r", newline='')
    gerardFile = open("Geralds Businesses.csv", "r", newline='')
    mergedFile = open("MergedLandscaping.txt", "w", newline='')
    
    geraldineReader = csv.reader(geraldineFile)
    gerardReader = csv.reader(gerardFile)
    mergedWriter = csv.writer(mergedFile)
    
    # Skip headers if your CSVs have them
    next(geraldineReader, None)
    next(gerardReader, None)
    
    readGeraldine()
    readGerard()
    checkEnd()

def readGeraldine():
    global geraldineNum, geraldineLastName, geraldineAddress, geraldineArea
    try:
        row = next(geraldineReader)
        geraldineNum = int(row[0])
        geraldineLastName = row[1]
        geraldineAddress = row[2]
        geraldineArea = int(row[3])
    except (StopIteration, IndexError):
        geraldineNum = END_NUM

def readGerard():
    global gerardNum, gerardLastName, gerardAddress, gerardArea
    try:
        row = next(gerardReader)
        gerardNum = int(row[0])
        gerardLastName = row[1]
        gerardAddress = row[2]
        gerardArea = int(row[3])
    except (StopIteration, IndexError):
        gerardNum = END_NUM

def checkEnd():
    global areBothAtEnd
    if geraldineNum == END_NUM:
        if gerardNum == END_NUM:
            areBothAtEnd = "Y"

def mergeRecords():
    if geraldineNum < gerardNum:
        mergedWriter.writerow([geraldineNum, geraldineLastName, geraldineAddress, geraldineArea])
        readGeraldine()
    else:
        mergedWriter.writerow([gerardNum, gerardLastName, gerardAddress, gerardArea])
        readGerard()
    checkEnd()

def finishUp():
    geraldineFile.close()
    gerardFile.close()
    mergedFile.close()

def main():
    getReady()
    while areBothAtEnd != "Y":
        mergeRecords()
    finishUp()
    print("Files merged successfully into MergedLandscaping.txt")

if __name__ == "__main__":
    main()