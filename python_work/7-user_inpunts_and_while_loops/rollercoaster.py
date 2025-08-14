height = input("How tall are you in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

"""
The program can compare height to 36 because height = int(height)
converts the input value to a numerical representation before the comparison is made. If the number entered is greater than or equal to 36, we tell 
the user that they’re tall enough:
"""