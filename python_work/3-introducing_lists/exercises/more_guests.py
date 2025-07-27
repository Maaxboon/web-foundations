"""
You just found a bigger dinner table, so now more space is available . Think of three more guests to invite to dinner 
"""
# Start with your program from Exercise 3-4 or Exercise 3-5 . Add a print statement to the end of your program informing people that you found a bigger dinner table.
guests = ['Messi', 'Linus', 'Curry']
message = " we found a bigger dinner table!"
print(f"Hello {guests[0]} {message}")
print(f"Hello {guests[1]} {message}")
print(f"Hello {guests[-1]} {message}")

# Use insert() to add one new guest to the beginning of your list.
guests.insert(0, 'Grisham')
# Use insert() to add one new guest to the middle of your list.
guests.insert(2, 'Fergie')
# Use append() to add one new guest to the end of your list.
guests.append("Webber")
# Print a new set of invitation messages, one for each person in your list
message1 = "Welcome to my dinner on August 24th at Villa Rosa Kempinski, Nairobi, Kenya "
print(message1 + guests[0])
print(message1 + guests[1])
print(message1 + guests[2])
print(message1 + guests[3])
print(message1 + guests[4])
print(message1 + guests[-1])