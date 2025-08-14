"""
7-2. Restaurant Seating: Write a program that asks the user how many people 
are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.
"""
people = input("How many people are in your dinner group? ")
people = int(people)

if people > 8:
    print(f"\nsince you are {people}, which is more than 8, You will have to wait for a table.")
else:
    print(f"You're table for {str(people)} is ready!")