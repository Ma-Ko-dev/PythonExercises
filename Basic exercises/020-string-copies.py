# Task: Write a Python program to get a string which is n (non-negative integer) copies of a given string.

def large_string(text, num):
    result = ""
    for i in range(1, num + 1):
        # capitalize it to make it more... nice looking? :D
        result += text.capitalize()
    return result


print(large_string("miau", 4))
