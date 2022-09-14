# Task: Write a Python program to calculate the sum of three given numbers, if the values are equal then return three
# times of their sum.

def calc_sum(num1, num2, num3):
    if num1 == num2 and num2 == num3:
        return (num1 + num2 + num3) * 3
    else:
        return num1 + num2 + num3


print(calc_sum(1, 2, 3))
print(calc_sum(1, 2, 3))
print(calc_sum(3, 3, 3))
