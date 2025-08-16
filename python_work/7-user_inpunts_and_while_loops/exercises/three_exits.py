"""
7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5 that do each of the following at least once:
•	 Use a conditional test in the while statement to stop the loop.
•	 Use an active variable to control how long the loop runs.
•	 Use a break statement to exit the loop when the user enters a 'quit' value.
"""
# Prompt users to enter their age
prompt = "\nWe need to know your age to determine how much you're paying."
prompt = "\nHow old are you? "

# under 3: free
while True:
    age = int(input(prompt))

    if age == 'quit':
        break
    elif age < 3:
        print("\nYou're ticket is free!")
        break
    elif age < 12:
        print("\nYou're ticket is $10")
        break
    # over 12: 15
    else:
        print("\nYou're ticket is $15")
        break 