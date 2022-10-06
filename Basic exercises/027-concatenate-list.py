# Task: Write a Python program to concatenate all elements in a list into a string and return it.

def foo(new_list: list) -> str:
    new_str = ""
    for e in new_list:
        new_str += str(e)
    return new_str


print(foo([1, 5, 12, 2]))
