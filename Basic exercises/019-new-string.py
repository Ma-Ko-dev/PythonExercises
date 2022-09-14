# Task: Write a Python program to get a new string from a given string where "Is" has been added to the front. If the
# given string already begins with "Is" then return the string unchanged.

def return_string(old_string):
    # Sample Solution
    # if len(old_string) >= 2 and old_string[:2] == "Is":
    #     return old_string
    # else:
    #     return "Is" + old_string

    # First solution CAN work, but can also fail if the String contains "Is" somewhere in the string
    # if "Is" in old_string:
    #     return old_string
    # else:
    #     return f"Is{old_string}"

    # Another attempt. In this attempt we remove leading whitespace before checking for "Is". We check the the char
    # at index 0 and 1 to be "Is". But just like in the sample solution, words like "Isometric" still kinda fell through
    old_string = old_string.lstrip()
    if old_string[0] == "I" and old_string[1] == "s":
        return old_string
    else:
        return f"Is{old_string}"


print(return_string("Here Is we go"))
print(return_string("Is this new"))
print(return_string("Isometric"))
print(return_string("IsArray"))
print(return_string("Empty"))
print(return_string("     Katze"))
print(return_string("     IsKatze"))

