"""
6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.
"""

favorite_numbers = {
    'maxtoshi' : [4,8],
    'deon' : [3,11],
    'kamart' : [5,33],
    'spinola' : [91,84],
    'zenretier' : [12,26],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for numbers in numbers:
        print(numbers)