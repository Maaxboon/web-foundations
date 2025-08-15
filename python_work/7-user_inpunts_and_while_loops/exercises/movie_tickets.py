"""
7-5. Movie Tickets: A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.
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