# PROBLEMS 26 to 30 — elif chains and ranges
#
# Every function RETURNS a value. No print, no input.
# Test with:  python3 week1/check.py
#
# These all sort a number into a category. Order matters in an elif chain:
# Python takes the FIRST branch that's true and skips the rest.


# PROBLEM 26: letter_grade(score)
# 90 and up is "A", 80 to 89 is "B", 70 to 79 is "C", 60 to 69 is "D", below 60 is "F".
#   letter_grade(95)  ->  "A"
#   letter_grade(85)  ->  "B"
#   letter_grade(75)  ->  "C"
#   letter_grade(65)  ->  "D"
#   letter_grade(50)  ->  "F"
#
# Hint: check the highest range first. If score >= 90 is checked first,
#       you don't need to write "and score < 100" anywhere.

def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
   




# PROBLEM 27: is_passing(score)
# Returns True if score is 60 or higher.
#   is_passing(60)  ->  True
#   is_passing(59)  ->  False
def is_passing(score):
    if score >= 60:
        return True
    else:
        return False




# PROBLEM 28: classify_temp(fahrenheit)
# Below 32 is "freezing", 32 to 59 is "cold", 60 to 79 is "warm", 80 and up is "hot".
#   classify_temp(20)  ->  "freezing"
#   classify_temp(45)  ->  "cold"
#   classify_temp(70)  ->  "warm"
#   classify_temp(95)  ->  "hot"
def classify_temp(fahrenheit): 
    if fahrenheit < 32:
        return "freezing"
    elif fahrenheit <= 59:
        return "cold"
    elif fahrenheit <= 79:
        return "warm"
    else:
        return "hot"


# PROBLEM 29: is_between(n, low, high)
# Returns True if n is between low and high, INCLUDING the ends.
#   is_between(5, 1, 10)   ->  True
#   is_between(15, 1, 10)  ->  False
#   is_between(1, 1, 10)   ->  True
#
# Hint: two conditions have to both be true. The word for that is "and".
def is_between(n, low, high):
    if n >= low and n <= high:
        return True
    else:
        return False





# PROBLEM 30: bmi_category(bmi)
# Below 18.5 is "underweight", 18.5 to 24.9 is "normal",
# 25 to 29.9 is "overweight", 30 and up is "obese".
#   bmi_category(17)  ->  "underweight"
#   bmi_category(22)  ->  "normal"
#   bmi_category(27)  ->  "overweight"
#   bmi_category(32)  ->  "obese"
def bmi_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"

