"""
You just found out that your new dinner table won’t 
arrive in time for the dinner, and you have space for only two guests
"""
# Start with your program from Exercise 3-6 . Add a new line that prints a message saying that you can invite only two people for dinner .
guests = ['Messi', 'Linus', 'Curry']

# Use insert() to add one new guest to the beginning of your list.
guests.insert(0, 'Grisham')
# Use insert() to add one new guest to the middle of your list.
guests.insert(2, 'Fergie')
# Use append() to add one new guest to the end of your list.
guests.append("Webber")
message = " I can only only invite two guests for dinner."
print(guests[0] + message)
print(guests[1] + message)
print(guests[2] + message)
print(guests[3] + message)
print(guests[4] + message)
print(guests[-1] + message)
# Use pop() to remove guests from your list one at a time until only two names remain in your list . Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.

# Remove first guest
minus_1 = guests.pop(0)
minus_message = " Sorry we have to reduce the guest list as we can only host 2."
print(minus_1 + minus_message)

# Remove second guest
minus_2 = guests.pop(1)
print(minus_2 + message)

# Remove Third guest
minus_3 = guests.pop(2)

# Remove fourth guest
minus_4 = guests.pop(-1)
print(guests)



# Print a message to each of the two people still on your list, letting them know they’re still invited.
still_in = " you're still on the guests' list."
print(guests[0] + still_in)
print(guests[1] + still_in)
# Use del to remove the last two names from your list, so you have an empty list. 
del guests[0]
del guests[0]

# Print your list to make sure you actually have an empty list at the end of your program
print(guests) 
