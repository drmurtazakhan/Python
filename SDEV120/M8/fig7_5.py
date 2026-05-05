# Constants
RAISE = 2.00

def housekeeping():
    infile = open("employeeData.txt", "r")
    outfile = open("updatedData.txt", "w")
    return infile, outfile

def detailLoop(infile, outfile, line):
    name, address, payRate = line.strip().split(",")
    payRate = float(payRate) + RAISE
    outfile.write(f"{name},{address},{payRate:.2f}\n")

def finish(infile, outfile):
    infile.close()
    outfile.close()

# Main program
def main():
    infile, outfile = housekeeping()

    for line in infile:   # while not eof
        detailLoop(infile, outfile, line)

    finish(infile, outfile)

# Run program
main()