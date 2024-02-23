import os

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "python_file.txt"
file_path = os.path.join(desktop_path, file_name)

with open(file_path, "w") as file:
    file.write("This file was created with python! \n")

print("Desktop file created successfully!")