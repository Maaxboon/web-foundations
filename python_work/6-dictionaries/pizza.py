# A list in a dictionary
# Store information about pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

# You can nest a list inside a dictionary any time you want more thanone value to be associated with a single key in a dictionary.