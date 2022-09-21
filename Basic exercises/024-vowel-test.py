# Task: Write a Python program to test whether a passed letter is a vowel or not.


def check_vowel(letter: str):
    vowels = "aeiou"
    letter.lower()
    if letter in vowels:
        return "Vowel detected."
    else:
        return "No Vowel detected."
    # alternative:
    # return letter in vowels


print(check_vowel("s"))
