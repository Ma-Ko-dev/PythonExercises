# Task: Write a Python program to accept a filename from the user and print the extension of that.
# For example: filename = abc.java Output: java
file_name = input("Please enter a Filename:\n")
# splitting the filename at the dot and creating a list.
extension = file_name.split(".")
# -1 is always the last object in the list. that's our file extension
print(f"The file Extension is: {extension[-1]}")
