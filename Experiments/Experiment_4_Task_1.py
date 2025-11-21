# ● Objective: The objective of this lab is to introduce the basic concepts of file
# operations in Python, covering:

# 1. File I/O Basics: Working with text files, CSV files, and binary files.
# 2. Exception Handling: Understanding how to handle file-related
# exceptions (both single and multiple).
# 3. Practical Applications: Writing and reading data from files and
# implementing basic file operations.



# ---- TEXT FILE OPERATIONS ----
try:
    # Writing to a text file
    with open("sample.txt", "w") as file:
        file.write("Hello, this is a simple text file.\n")
        file.write("We are learning file handling in Python!\n")
    print("Data written successfully to sample.txt")

    # Reading from the text file
    with open("sample.txt", "r") as file:
        content = file.read()
        print("\n--- File Content ---")
        print(content)

except FileNotFoundError:
    print("Error: The file was not found.")
except IOError:
    print("Error: Could not read or write the file.")
