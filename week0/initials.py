# PROBLEM 4: Initials
#
# Write a function called initials(full_name) that takes a full name
# and returns the initials with periods, capitalized.
#
# Examples:
#   initials("maia rowe")    should return  "M.R."
#   initials("ada lovelace") should return  "A.L."
#   initials("grace hopper") should return  "G.H."
#
# Test it with at least three different names.
#
# Concepts: .split(), .upper(), string indexing, return
#
# Hint: .split() turns "maia rowe" into a list of two words.
#       You can grab the first character of a word with word[0].


# Your code below:
# 1. Promt user for input
# 2. Strip letters except first letters
# 3. Capitilize both letters
# 4. Print results to console
def main():
     full_name = input("Enter your name \n")
     print(initials(full_name))

def initials(full_name):
    words = full_name.split()

    first_letter = words[0][0].upper()
    second_letter = words[1][0].upper()

    return f"{first_letter}.{second_letter}."


main()

