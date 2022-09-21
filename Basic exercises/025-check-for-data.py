# Task: Write a Python program to check whether a specified value is contained in a group of values.
# Test Data:
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False


def check_value(value: int, group: list):
    return value in group


print(check_value(3, [1, 5, 8, 3]))
print(check_value(-1, [1, 5, 8, 3]))
