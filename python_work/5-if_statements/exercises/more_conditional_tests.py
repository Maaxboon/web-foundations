"""
5-2. More Conditional Tests: You don’t have to limit the number of tests you create to 10 . If you want to try more comparisons, write more tests and add them to conditional_tests.py . Have at least one True and one False result for each of the following:
 •	Tests for equality and inequality with strings
 •	Tests using the lower() function
 •	Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
 •	Tests using the and keyword and the or keyword
 •	Test whether an item is in a list
 •	Test whether an item is not in a list
"""

# Test inequality with strings
# Assign a value maxtoshi to a variable first_name
first_name = 'Maxtoshi'
# test for inequality
print(first_name == 'Maxtoshi') # True

# test for equality
print(first_name == 'maxtoshi') # False

# test using the lower() function
print(first_name.lower() == 'maxtoshi')

# Numerical tests:
captains_alu = 2
captains_ala = 3
# equality
print(captains_alu == captains_ala)
# inequality
print(captains_alu != captains_ala)
# greater than and less than
print(captains_alu > captains_ala)
print(captains_alu < captains_ala)
# greater than or equal to
print(captains_alu >= captains_ala)
print(captains_alu <= captains_ala)

# keyword tests
# and
alu_owner = 'swaniker'
alche_owner = 'swaniker'
print("Fred Swaniker in the owner of ALU and ALCHE:")
print(alu_owner == 'swaniker') and (alche_owner == 'swaniker')

# or
# test whether an item is in a list
# test whether an item is not in a list