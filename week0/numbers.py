# PROBLEMS 6 to 10 — number functions
#
# Write each function so it RETURNS a value. Do not print inside them.
# Test with:  python3 week0/check.py


# PROBLEM 6: double(n)
# Returns the number doubled.
#   double(5)    ->  10
#   double(2.5)  ->  5.0
def double(n):
  return n * 2





# PROBLEM 7: area_of_rectangle(width, height)
# Returns the area.
#   area_of_rectangle(4, 5)   ->  20
#   area_of_rectangle(2.5, 4) ->  10.0
def  area_of_rectangle(width, height):
 return width * height




# PROBLEM 8: seconds_to_minutes(seconds)
# Returns how many minutes that is.
#   seconds_to_minutes(90)   ->  1.5
#   seconds_to_minutes(120)  ->  2.0

def seconds_to_minutes(seconds):
  return seconds / 60




# PROBLEM 9: average(a, b, c)
# Returns the average of three numbers.
#   average(3, 4, 5)   ->  4.0
#   average(10, 20, 0) ->  10.0
def average(a, b, c):
  return (a + b + c) / 3
  




# PROBLEM 10: percent_of(part, whole)
# Returns what percent `part` is of `whole`.
#   percent_of(25, 200)  ->  12.5
#   percent_of(50, 50)   ->  100.0
#
# Hint: part divided by whole, times 100.

def percent_of(part, whole):
  return (part / whole) * 100