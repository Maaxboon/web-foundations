"""
7-3. Multiples of Ten: Ask the user for a number, and then report whether the 
number is a multiple of 10 or not.
"""
number = input("Enter a number and I will tell you if it is a multiple of 10 or not: ")
number = int(number)

if number % 10 == 0:
    print(f"\n{str(number)} is a multiple of 10!")
else:
    print(f"\n{str(number)} is not a multiple of 10.")