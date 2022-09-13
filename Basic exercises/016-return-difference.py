# Task: Write a Python program to get the difference between a given number and 17, if the number is greater than 17
# return double the absolute difference.

def return_difference(num):
    if num > 17:
        return (num - 17) * 2
    else:
        return 17 - num


print(return_difference(12))
print(return_difference(66))
