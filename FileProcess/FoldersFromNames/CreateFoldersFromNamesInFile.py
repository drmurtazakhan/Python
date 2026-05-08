import os

# Absolute path to your names.txt file
file_path = r"K:\0MAK\RW\PythonKhan\FileProcess\FoldersFromNames\names.txt"

# Read folder names from file
with open(file_path, "r") as f:
    folders = [line.strip() for line in f if line.strip()]

# Create each folder
for folder in folders:
    os.makedirs(folder, exist_ok=True)

print("Folders created successfully from names.txt!")
