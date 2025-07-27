"""
You just heard that one of your guests can’t make the 
dinner, so you need to send out a new set of invitations . You’ll have to think of 
someone else to invite 
"""
# Print a second set of invitation messages, one for each person who is still in your list 
guests = ['Messi', 'Linus', 'Curry']
message = "Welcome to my dinner on August 24th at Villa Rosa Kempinski, Nairobi, Kenya "
print(message + guests[0])
print(message + guests[1])
print(message + guests[-1])

# Start with your program from Exercise 3-4 . Add a print statement at the end of your program stating the name of the guest who can’t make it.
print(guests[-1] + " will not make it for the dinner.")

# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
guests[-1] = 'Jordan'
print(message + guests[0])
print(message + guests[1])
print(message + guests[-1])
