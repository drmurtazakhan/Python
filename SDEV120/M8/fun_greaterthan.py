# Function definition
def greater_than(x, y):
    if x > y:
        return True
    else:
        return False


# Main program
a = 2
b = 3

result = greater_than(a, b)

print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result).lower())


# Test case 2 (as required)
a = 10
b = 6

result = greater_than(a, b)

print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result).lower())