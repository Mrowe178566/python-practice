# PROBLEMS 16 to 20 — the harder five
#
# Write each function so it RETURNS a value. Do not print inside them.
# Test with:  python3 week0/check.py


# PROBLEM 16: shout(text)
# Returns the text in all caps with an exclamation mark on the end.
#   shout("hello")      ->  "HELLO!"
#   shout("i did it")   ->  "I DID IT!"

def shout(text):
    return (f"{text.upper()}!")



# PROBLEM 17: initials_three(full_name)
# Same as your initials problem, but for THREE names.
#   initials_three("mary jane smith")   ->  "M.J.S."
#   initials_three("ada byron lovelace") ->  "A.B.L."
#
# This is the one you struggled with, one level up. If you can do this
# cold, the original is genuinely locked in.

#thing to Do
#write a function with full_name passed through
#take the users first,middle,last name
#Take the first letter capitilize it 
#return the three letter with a period between each

def initials_three(full_name):
    first_name = full_name.split()[0][0]
    middle_name = full_name.split()[1][0]
    last_name = full_name.split()[2][0]
    return f"{first_name}.{middle_name}.{last_name}.".upper()


# PROBLEM 18: reverse_name(full_name)
# Returns "Last, First" with both capitalized.
#   reverse_name("maia rowe")     ->  "Rowe, Maia"
#   reverse_name("ada lovelace")  ->  "Lovelace, Ada"

#Things to do
#create function reverse_name(full_name)
#reverse the order of the name "Maia Rowe"->  "Rowe, Maia"
#then return ->  "Rowe, Maia"
def reverse_name(full_name):
   first_backwards = full_name.split()[0].capitalize()
   last_backwards = full_name.split()[1].capitalize()
   return f"{last_backwards}, {first_backwards}"





# PROBLEM 19: price_with_tax(price, tax_rate)
# Returns the total as a formatted string with a dollar sign
# and two decimal places. tax_rate is a decimal, so 0.0875 means 8.75%.
#   price_with_tax(100, 0.0875)  ->  "$108.75"
#   price_with_tax(20, 0.10)     ->  "$22.00"

#Things to do
#create function price_with_tax(price, tax_rate)
# add the price and tax
#Returns the total as a formatted string with a dollar sign
#and two decimal places. tax_rate is a decimal, so 0.0875 means 8.75%.
def price_with_tax(price, tax_rate):
    tip = price * tax_rate       
    final_amount = tip + price
    return f"${final_amount:.2f}"




# PROBLEM 20: format_phone(digits)
# Takes 10 digits as a string, returns a formatted phone number.
#   format_phone("3125551234")  ->  "(312) 555-1234"
#   format_phone("8005551212")  ->  "(800) 555-1212"
#
# Hint: you can grab a RANGE of characters with text[start:end].
#       "python"[0:3] gives "pyt". The end number is not included.

def format_phone(digits):
    first_three = digits[0:3]
    second_three = digits[3:6]
    third_four = digits[6:]
    return f"({first_three}) {second_three}-{third_four}"
