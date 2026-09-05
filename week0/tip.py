# PROBLEM 2: Tip calculator
#
# Ask for a bill amount and a tip percentage.
# Print the total, rounded to two decimal places.
#
# Example run:
#   Bill: 47.50
#   Tip percent: 20
#   Total: $57.00
#
# Concepts: float(), arithmetic, number formatting inside an f-string
#
# Hint: input() always gives you a string, even when the user types a number.
#       You'll need to convert it before you can do math with it.


# Your code below:

def main():
    dollars = dollars_to_float(input(("How much was the meal? \n")))
    percent = percent_to_float(input(("What percentage would you like to tip? \n")))
    tip = dollars * percent
    final_amount = tip + dollars
    print(f"Total: ${final_amount:.2f}")


def dollars_to_float(dollars):
    bill_amount = dollars.replace("$","")
    final_amount = float(bill_amount)
    return final_amount



def percent_to_float(percent):
    percentage_amount = percent.replace("%","")
    final_percent = float(percentage_amount) / 100
    return final_percent




main()
