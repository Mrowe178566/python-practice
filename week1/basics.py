# PROBLEMS 21 to 25 — if / else basics
#
# Every function RETURNS a value. No print, no input.
# Test with:  python3 week1/check.py
#
# New this week: if, elif, else, comparison operators (== != < > <= >=),
# and the modulo operator % which gives you the remainder after division.


# PROBLEM 21: is_positive(n)
# Returns True if n is greater than zero, otherwise False.
#   is_positive(5)   ->  True
#   is_positive(-5)  ->  False
#   is_positive(0)   ->  False
#
# Hint: a comparison like n > 0 already IS True or False. You can return it directly.

def is_positive(n):
    if n > 0:
        return  True
    else:
        return False



# PROBLEM 22: is_even(n)
# Returns True if n is even, otherwise False.
#   is_even(4)  ->  True
#   is_even(7)  ->  False
#
# Hint: n % 2 gives the remainder when n is divided by 2.
#       Even numbers have remainder 0.

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False



# PROBLEM 23: bigger(a, b)
# Returns whichever number is larger.
#   bigger(3, 7)   ->  7
#   bigger(10, 2)  ->  10

def bigger(a, b):
    if a > b:
        return a



# PROBLEM 24: is_adult(age)
# Returns True if age is 18 or older.
#   is_adult(18)  ->  True
#   is_adult(17)  ->  False

def is_adult(age):
    if age >= 18:
        return True
    else:
        return False



# PROBLEM 25: sign(n)
# Returns "positive", "negative", or "zero".
#   sign(5)   ->  "positive"
#   sign(-5)  ->  "negative"
#   sign(0)   ->  "zero"
#
# This one needs three branches: if, elif, else.
def sign(n):
    if n == 0:
        return "zero"
    elif n > 0:
        return "positive"
    else:
        return "negative"