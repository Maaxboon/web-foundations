"""
 4-1. Pizzas: Think of at least three kinds of your favorite pizza . Store these pizza names in a list, and then use a for loop to print the name of each pizza .
 •	Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza . For each pizza you should have one line of output containing a simple statement like I like pepperoni pizza .
 •	Add a line at the end of your program, outside the for loop, that states how much you like pizza . The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
"""
# List of four pizzas in Nairobi
pizzas = ['Pepperoni', 'Cheeseburger', 'Hawaiian', 'Spicy Peri-Peri']

# A for loop for looping through the list
for pizza in pizzas:
    # Printing the pizzas
    print(pizza)

    # Printing the pizzas with a message
    print("You can have " + pizza + " pizza in Nairobi.\n")

# Final lines about loving pizza
print("\nPepperoni pizza is my go-to when hanging out with friends.")
print("Cheeseburger pizza always surprises me with its flavor combo.")
print("Spicy Peri-Peri pizza is perfect for when I'm craving heat.")
print("I really love pizza!")