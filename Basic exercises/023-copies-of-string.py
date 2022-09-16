# Task:  Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given
# string. Return the n copies of the whole string if the length is less than 2.

def foo(text, copies):
    chars = text[:2]

    if len(text) < 2:
        return text * copies
    else:
        return chars * copies


print(foo("p", 5))
