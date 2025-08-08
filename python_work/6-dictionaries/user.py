# Looping Through All Key-Value Pairs
"""
Before we explore the different approaches to looping, let’s consider a new dictionary designed to store information about a user on a website. 
The following dictionary would store one person’s username, first name, and last name:
"""
user_0 = {
    'username' : 'efermi',
    'first' : 'enrico',
    'last' : 'fermi',
}

"""
You can access any single piece of information about user_0 based on what you’ve already learned in this chapter. But what if you wanted to see everything stored in this user’s dictionary? To do so, you could through the dictionary using a for loop:
"""
# to write a for loop for a dictionary, you create names for the two variables that will hold the key and value in each key-value pair. You can choose any names you want for these two variables.
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)