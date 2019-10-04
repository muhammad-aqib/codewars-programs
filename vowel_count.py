# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, and u as vowels for this Kata.
# The input string will only consist of lower case letters and/or spaces.


def getCount(inputStr):
    num_vowels = 0
    vowels = ["a", "e", "i", "o", "u"]
    for i in range(len(inputStr)):
        if inputStr[i] in vowels:
            num_vowels += 1

    return num_vowels


if __name__ == "__main__":
    print(getCount("aksjd nba sd"))
