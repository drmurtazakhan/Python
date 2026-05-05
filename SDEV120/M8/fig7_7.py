# Declarations
TITLE = "Company Clients by State of Residence"
COL_HEADS = "Name   City   State"

count = 0
oldState = ""

# Global variables (to mimic pseudocode style)
inFile = None
name = ""
city = ""
state = ""

def getReady():
    global inFile, name, city, state, oldState

    print(TITLE)
    print(COL_HEADS)

    inFile = open("ClientsByState.txt", "r")

    line = inFile.readline()
    if line:
        name, city, state = [x.strip() for x in line.split(",")]
        oldState = state

def produceReport():
    global name, city, state, count, oldState

    if state != oldState:
        controlBreak()

    print(name, city, state)
    count = count + 1

    line = inFile.readline()
    if line:
        name, city, state = [x.strip() for x in line.split(",")]
    else:
        # Mark EOF by clearing state
        state = ""

def controlBreak():
    global count, oldState, state

    print("Count for", oldState, count)
    count = 0
    oldState = state

def finishUp():
    global inFile, count, oldState

    print("Count for", oldState, count)
    inFile.close()


# Main program
def main():
    global state

    getReady()

    while state != "":   # while not eof
        produceReport()

    finishUp()


# Run program
main()