magicians = ['alice', 'david', 'carolina'] # We begin by defining a list
for magician in magicians: # This line tells Python to pull a name from the list magicians, and store it in the variable magician
    # print("\n" + magician) #  we tell Python to print the name that was just stored in magician

# Doing more work within a for loop
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick " + magician.title() + ".\n")

# Doing something after a for loop
print("Thank you everyone. That was a great magic show.")
