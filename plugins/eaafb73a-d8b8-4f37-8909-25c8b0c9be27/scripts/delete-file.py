import os

file_path = os.path.expanduser("~/Desktop/python_file.txt")

if os.path.exists(file_path):
    os.remove(file_path)
    print("File has been removed.")
else:
    print("File does not exist.")