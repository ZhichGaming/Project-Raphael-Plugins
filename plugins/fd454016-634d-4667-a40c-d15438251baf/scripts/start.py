import os

# Get the path to the desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Create the file path
file_path = os.path.join(desktop_path, "python.txt")

# Open the file in write mode
with open(file_path, "w") as file:
    # Write some content to the file
    file.write("This is a text file created with Python!")

# Print a message to confirm the file creation
print("File 'python.txt' has been created on the desktop.")
