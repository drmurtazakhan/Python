import requests

# The URL for your enabled EMP table
# Note: Added an extra forward slash at the end, which Oracle REST services often prefer
url = "https://apex.oracle.com/pls/apex/schema28/emp/"

try:
    # Send a GET request to fetch the table data
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        print("Success! Here is the data from your EMP table:\n")
        print(data)
    else:
        print(f"Failed to connect. Status Code: {response.status_code}")
        print(response.text)

except Exception as e:
    print(f"An error occurred: {e}")