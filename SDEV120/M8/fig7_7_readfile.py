# --- Declarations ---
TITLE = "Company Clients by State of Residence"
COL_HEADS = "{:<15} {:<15} {:<15}".format("Name", "City", "State")
name = ""
city = ""
state = ""

count = 0
oldState = ""
inFile = None  # This will hold our file object


def getReady():
    global name, city, state, oldState, inFile
    print(TITLE)
    print(COL_HEADS)

    # open inFile "ClientsByState.txt"
    try:
        inFile = open("ClientsByState.txt", "r")
        # input name, city, state from inFile (Priming Read)
        line = inFile.readline()
        if line:
            # We split the line by commas to get our three variables
            name, city, state = line.strip().split(",")
            oldState = state
        else:
            name = "EOF"
    except FileNotFoundError:
        print("Error: The data file was not found.")
        name = "EOF"


def produceReport():
    global name, city, state, count, oldState, inFile

    # Check if the state has changed (Control Break)
    if state != oldState:
        controlBreak()

    # output name, city, state
    print("{:<15} {:<15} {:<15}".format(name, city, state))
    count = count + 1

    # input name, city, state from inFile
    line = inFile.readline()
    if line:
        name, city, state = line.strip().split(",")
    else:
        name = "EOF"


def controlBreak():
    global count, oldState, state
    # output subtotal for the previous state
    print("{:>40}{:>5}".format("Count for " + oldState, count))
    count = 0
    oldState = state


def finishUp():
    global count, oldState, inFile
    # output final state total
    if count > 0:
        print("{:>40}{:>5}".format("Count for " + oldState, count))

    # close inFile
    if inFile:
        inFile.close()


# --- Mainline Logic ---
getReady()
while name != "EOF":  # while not eof
    produceReport()
finishUp()
