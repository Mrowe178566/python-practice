# PROBLEM 3: Temperature function
#
# Write a function called celsius_to_fahrenheit(c) that takes a celsius
# temperature and RETURNS the fahrenheit value.
#
# Do NOT print inside the function. It should return, and the printing
# happens outside. That distinction is the whole point of this one.
#
# Then ask the user for a celsius temp and print the result.
#
# Formula: f = c * 9/5 + 32
#
# Example run:
#   Celsius: 100
#   212.0
#
# Concepts: def, parameters, return vs print

#Notes
# ask user to input celsius temp
# convert celsius to fahrenheit (Formula: f = c * 9/5 + 32)
# print fahrenheit result 

# Your code below:
def main():
    celsius = input("Enter celsisus temperature to convert to fahrenheit \n")
    print(celsius_to_fahrenheit(celsius))
    
   

def celsius_to_fahrenheit(celsius):
    fahrenheit = int(celsius) * 9/5 + 32
    return fahrenheit



main()
