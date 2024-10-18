def gcd(a, b):
    """Calculate the GCD of two numbers using the Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a

# Example usage
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {result}.")



## ResearchGate: http://www.researchgate.net/profile/Murtaza_Khan2/
## LinkedIn: https://www.linkedin.com/in/dr-murtaza-ali-khan-3b368019
## Google Scholar: https://scholar.google.com/citations?user=n0JDQ0sAAAAJ
## Scopus: https://www.scopus.com/authid/detail.uri?authorId=7410318323
## GitHub: https://github.com/drmurtazakhan
