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

# Note:  Most of the conditional expressions you write will test for equality, but sometimes you’ll find it more efficient to test for inequality.