# PROBLEMS 31 to 35 — and, or, not
#
# Every function RETURNS a value. No print, no input.
# Test with:  python3 week1/check.py
#
# Combining conditions:
#   a and b     true only if BOTH are true
#   a or b      true if EITHER is true
#   not a       flips it


# PROBLEM 31: can_vote(age, is_citizen)
# Returns True only if age is 18 or older AND is_citizen is True.
#   can_vote(18, True)   ->  True
#   can_vote(17, True)   ->  False
#   can_vote(30, False)  ->  False





# PROBLEM 32: is_weekend(day)
# Returns True if day is Saturday or Sunday. Should work regardless of capitalization.
#   is_weekend("saturday")  ->  True
#   is_weekend("Sunday")    ->  True
#   is_weekend("monday")    ->  False
#
# Hint: lowercase the input first so you only have to compare against one spelling.





# PROBLEM 33: same_sign(a, b)
# Returns True if both numbers are positive or both are negative.
#   same_sign(3, 5)    ->  True
#   same_sign(-2, -8)  ->  True
#   same_sign(3, -5)   ->  False
#
# Hint: this is two "and" conditions joined by an "or".





# PROBLEM 34: is_leap_year(year)
# A year is a leap year if it's divisible by 4,
# EXCEPT years divisible by 100 are not,
# EXCEPT years divisible by 400 are.
#   is_leap_year(2024)  ->  True    (divisible by 4)
#   is_leap_year(1900)  ->  False   (divisible by 100, not 400)
#   is_leap_year(2000)  ->  True    (divisible by 400)
#   is_leap_year(2023)  ->  False
#
# This is a classic. Check the most specific rule (400) first.





# PROBLEM 35: fizzbuzz(n)
# Returns "FizzBuzz" if n is divisible by both 3 and 5,
# "Fizz" if divisible by 3 only, "Buzz" if divisible by 5 only,
# otherwise the number itself as a string.
#   fizzbuzz(3)   ->  "Fizz"
#   fizzbuzz(5)   ->  "Buzz"
#   fizzbuzz(15)  ->  "FizzBuzz"
#   fizzbuzz(7)   ->  "7"
#
# This is the single most famous interview screening question in software.
# The trap: check "both" BEFORE checking either one alone, or 15 will
# match the Fizz branch and stop there.
# Hint: str(7) turns a number into "7".
