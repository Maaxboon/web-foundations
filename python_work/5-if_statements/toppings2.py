# using if statements with lists
# Checking for Special Items

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    #  checks to see if the person requested green peppers
    if requested_topping == 'green peppers': 
        print(("Sorry, we are out of green peppers right now."))
    # ensures that all other toppings will be added to the pizza
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

# Checking That a List Is Not Empty

# we start out with an empty list of requested toppings
requested_toppings = []

#  quick check 
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
#  If the conditional test fails, we print a message asking the customer if they really want a plain pizza with no toppings
else:
    print("Are you sure you want an empty pizza?")
"""
If the list is not empty, the output will show each requested topping being added to the pizza.
"""

# Using Multiple Lists
# we define a list of available toppings at this pizzeria
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

# we make a list of toppings that a customer has requested
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# we loop through the list of requested toppings
for requested_topping in requested_toppings:
    #  we first check to see if each requested topping is actually in the list of available toppings  If it is, we add that topping to the pizza
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    # prints a message telling the user which toppings are unavailable.
    else:
        print("Sorry, we don't have " + requested_topping)
    
print("\nFinished making your pizza!")