# Task: Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and
# a tuple with those numbers.

user_input = input("Please enter some comma-seperated numbers:\n")
# split() returns a list from a string, splitting each letter at the ", "
new_list = user_input.split(", ")
# tuple() creates a new tuple from an iterable object, like a list, which split() returns
new_tuple = tuple(new_list)

print(f"New List: {new_list}")
print(f"New Tuple: {new_tuple}")
