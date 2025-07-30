"""
4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
 •	Print the message, The first three items in the list are: . Then use a slice to print the first three items from that program’s list .
 •	Print the message, Three items from the middle of the list are: . Use a slice to print three items from the middle of the list .
 •	Print the message, The last three items in the list are: . Use a slice to print the last three items in the list 
"""
# List of institutions under the African Leadership Group
institutions = ['ala', 'alc', 'alu','alx', 'alche']

# First three institutions
print("The first three institutions are:")
print(institutions[:3])

# Middle three institutions
print("\nThree items from the middle of the list are:")
print(institutions[1:4])

# Last three institutions
print("\nThe last three items in the list are:")
print(institutions[-3:])