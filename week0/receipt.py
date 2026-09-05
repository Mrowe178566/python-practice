# PROBLEM 5: Receipt
#
# Write a function receipt(item, price, quantity) that returns a
# formatted line for a receipt.
#
# Examples:
#   receipt("Coffee", 4.50, 3)   should return  "3x Coffee = $13.50"
#   receipt("Bagel", 2.25, 2)    should return  "2x Bagel = $4.50"
#
# Call it a few times with different values and print the results.
#
# Concepts: multiple parameters, doing math inside a function,
#           f-strings with 2-decimal formatting
#
# This one combines everything from problems 1 through 4.

#NOTES 
# Take 3 inputs from user: Item name, price, and quantity
# Calculate quantity x price 
# return the final price

# Your code below:

def main():
    item = input("Enter item name \n")
    price = input((f"Whats {item} price? \n"))
    quantity = input((f"How many {item} are in cart? \n"))
    print(receipt(item, price, quantity))

def receipt(item, price, quantity):
        item_name = item
        price_amount = float(price)
        quantity_amount = int(quantity)
        total_amount = (quantity_amount * price_amount)
        return (f"{quantity_amount}x {item_name} = ${total_amount:.2f}")
    


main()

    
