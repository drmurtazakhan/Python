def factorial_iterative(n):
    """Calculate the factorial of a number iteratively."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage
number = int(input("Enter a number: "))
result = factorial_iterative(number)
print(f"The factorial of {number} is {result}.")



## ResearchGate: http://www.researchgate.net/profile/Murtaza_Khan2/
## LinkedIn: https://www.linkedin.com/in/dr-murtaza-ali-khan-3b368019
## Google Scholar: https://scholar.google.com/citations?user=n0JDQ0sAAAAJ
## Scopus: https://www.scopus.com/authid/detail.uri?authorId=7410318323
## GitHub: https://github.com/drmurtazakhan
