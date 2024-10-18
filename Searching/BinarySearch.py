def binary_search(arr, target):
    """Perform binary search on a sorted array."""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore right half
        else:
            right = mid - 1
            
    return -1  # Target not found

# Example usage
sorted_array = [10, 21, 32, 46, 52, 69, 78, 89, 90]
target_value = int(input("Enter the number to search for: "))
result = binary_search(sorted_array, target_value)

if result != -1:
    print(f"Element found at index {result}.")
else:
    print("Element not found in the array.")


## ResearchGate: http://www.researchgate.net/profile/Murtaza_Khan2/
## LinkedIn: https://www.linkedin.com/in/dr-murtaza-ali-khan-3b368019
## Google Scholar: https://scholar.google.com/citations?user=n0JDQ0sAAAAJ
## Scopus: https://www.scopus.com/authid/detail.uri?authorId=7410318323
## GitHub: https://github.com/drmurtazakhan
