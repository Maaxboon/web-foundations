# Simple if statements
age_0 = 19
if age_0 >= 18: # Python checks to see whether the value in age is greater than or equal to 18. 
    print("You're old eneough to vote!") #  It is, so Python executes the indented print statement
    print("Have you registered to vote yet?") # Checks if a person has registered as a voter

# If-else statements
age_1 = 17
if age_1 >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("\nSorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# The if-elif-else Chain
age_park = 12
if age_park < 4: #  tests whether a person is under 4 years old
        print("\nYour admission cost is $0.")
elif age_park < 18: #  tests whether a person is unover  4 years old but less than 18
     print("\nYour admission is $5.")
else:
     print("\nYour admission is $10.")

"""
Rather than printing the admission price within the if-elif-else block, it would be more concise to set just the price inside the if-elif-else chain and then have a simple print statement that runs after the chain has been evaluated:
"""

age_park = 12
if age_park < 4:
     price = 0
elif age_park < 18:
     price = 5
else:
     price = 10

print("Your admission cost is $" + str(price) + ".")

# Using Multiple elif Blocks

age_park = 12

if age_park < 4:
     price = 0
elif age_park < 18:
     price = 5
elif age_park < 65:
     price = 10
elif age_park >= 65:
     price = 5

print("You admission cost is $" + str(price) + ".")
