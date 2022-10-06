# Task: Write a Python program to create a histogram from a given list of integers.

def create_histogram(numlist: list) -> None:
    for num in numlist:
        for _ in range(num):
            print("*", end=" ")
        print("\r")


create_histogram([2, 3, 6, 5])
