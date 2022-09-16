# Task: Write a Python program to find whether a given number (accept from the user) is even or odd, print out an
# appropriate message to the user.

def check_num(num):
    if num % 2 == 0:
        print(f"{num} is an even Number.")
    else:
        print(f"{num} is not an even Number.")


check_num(int(input("Please type a Number to be checked: ")))
