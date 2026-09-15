# PROBLEMS 36 to 40 — realistic mini-problems
#
# Every function RETURNS a value. No print, no input.
# Test with:  python3 week1/check.py
#
# These look like things you'd actually be asked to write. Each one
# combines a conditional with a little arithmetic or formatting.


# PROBLEM 36: shipping_cost(order_total)
# Shipping is free on orders of $50 or more, otherwise it's $5.99.
#   shipping_cost(60)  ->  0
#   shipping_cost(30)  ->  5.99

def shipping_cost(order_total):
    if order_total >= 50:
        return 0
    return 5.99
   



# PROBLEM 37: ticket_price(age)
# Children under 12 pay $8. Seniors 65 and over pay $10. Everyone else pays $15.
#   ticket_price(8)   ->  8
#   ticket_price(30)  ->  15
#   ticket_price(70)  ->  10
def  ticket_price(age):
    if age < 12:
        return 8
    elif age >= 65:
        return 10
    else:
        return 15
      





# PROBLEM 38: discount(price, is_member)
# Members get 10% off. Non-members pay full price.
#   discount(100, True)   ->  90.0
#   discount(100, False)  ->  100

def discount(price, is_member):
    if is_member:
        return  price - price * 0.10
    else:
        return price



# PROBLEM 39: parking_fee(hours)
# The first hour is free. Every hour after that costs $3.
#   parking_fee(1)  ->  0
#   parking_fee(2)  ->  3
#   parking_fee(4)  ->  9

def parking_fee(hours):
    if hours <= 1:
        return 0
    else:
        return (hours - 1) * 3
        



# PROBLEM 40: describe_number(n)
# Returns a description combining even/odd and positive/negative.
# Zero is a special case and just returns "zero".
#   describe_number(4)   ->  "even and positive"
#   describe_number(-3)  ->  "odd and negative"
#   describe_number(-8)  ->  "even and negative"
#   describe_number(0)   ->  "zero"
#
# This combines everything from this week: modulo, comparison,
# multiple branches, and building a string from the results.

#Thing to do
# "even and positive"
# "odd and negative"
# "even and negative"
# "zero"

def describe_number(n):
    if n == 0:
        return "zero"
    parity = "even" if n % 2 == 0 else "odd"
    sign = "positive" if n > 0 else "negative"
    return f"{parity} and {sign}" 
    
    