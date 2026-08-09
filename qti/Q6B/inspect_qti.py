import os

print("--- Listing contents of 'items' folder ---")
for root, dirs, files in os.walk("./items"):
    print(f"Directory: {root}")
    for file in files:
        print(f"  - File: {file}")