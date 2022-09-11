# Task:  Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
user_data = int(input("Please input an integer: "))
num1 = int(f"{user_data}")
num2 = int(f"{user_data}{user_data}")
num3 = int(f"{user_data}{user_data}{user_data}")
result = num1 + num2 + num3
print(result)
