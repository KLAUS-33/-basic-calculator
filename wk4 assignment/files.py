#File Read & Write Challenge 🖋️: Read a file and write a modified version to a new file
try:
    filename = input("Enter the filename to read: ")
    with open(filename, "r") as file:
        content = file.read()
    
    modified_content = content.upper()  # Example modification
    
    with open("modified_" + filename, "w") as new_file:
        new_file.write(modified_content)
    print("Modified file created successfully!")
except FileNotFoundError:
    print("Error: File not found.")
except IOError:
    print("Error: Unable to read the file.")
