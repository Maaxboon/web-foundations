# Checking Inequality
"""
When you want to determine whether two values are not equal, you can combine an exclamation point and an equal sign (!=). The exclamation point represents not, as it does in many programming languages.
Let’s use another if statement to examine how to use the inequality operator. We’ll store a requested pizza topping in a variable and then print a message if the person did not order anchovies:
"""

# Declares a variable to store the requested topping
requested_topping = 'mushrooms'

# compares the value of requested_topping to the value 'anchovies'
#  If these two values do not match, Python returns True and executes the code following the if statement. If the two values match, Python returns False and does not run the code following the if statement.
if requested_topping != 'anchovies':
    # Because the value of requested_topping is not 'anchovies', the print statement is executed:
    print("Hold the anchovies!")

# Note:  Most of the conditional expressions you write will test for equality, but sometimes you’ll find it more efficient to test for inequality

# Checking Whether a Value is in a List
"""
Sometimes it’s important to check whether a list contains a certain value before taking an action. For example, you might want to check whether a new username already exists in a list of current usernames before completing someone’s registration on a website. In a mapping project, you might want to check whether a submitted location already exists in a list of known 
locations.
To find out whether a particular value is already in a list, use the keyword in. Let’s consider some code you might write for a pizzeria. We’ll make a list of toppings a customer has requested for a pizza and then check whether certain toppings are in the list.
"""

# Checking Whether a Value is in a List
"""
Sometimes it’s important to check whether a list contains a certain value before taking an action. For example, you might want to check whether a new username already exists in a list of current usernames before completing someone’s registration on a website. In a mapping project, you might want to check whether a submitted location already exists in a list of known 
locations.
To find out whether a particular value is already in a list, use the keyword in. Let’s consider some code you might write for a pizzeria. We’ll make a list of toppings a customer has requested for a pizza and then check whether certain toppings are in the list.
"""

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

"""
the keyword in tells Python to check for the existence of 'mushrooms' and 'pepperoni' in the list requested_toppings. This technique is quite powerful because you can create a list of essential values, and then easily check whether the value you’re testing matches one of the values in the list.
"""