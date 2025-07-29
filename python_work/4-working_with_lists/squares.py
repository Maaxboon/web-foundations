# We start with an empty list called squares
squares = []

# we tell Python to loop through each value from 1 to 10 using the range() function.
for value in range(1,11):

    # Inside the loop, the current value is raised to the second power and stored in the variable square
    square = value ** 2

    # each new value of square is appended to the list squares
    squares.append(square)

    # To write this code more concisely, omit the temporary variable square and append each new value directly to the list:
    # squares.append(value ** 2)

#  Finally, when the loop has finished running, the list of squares is printed 

print("The squares of numbers between 0 and 11 are:")
print(squares)

# We start with an empty list called cubes
cubes = []

# We tell python to loop through each value from 1 to 5
for i in range(1,6):

    # Inside the loop, the current value is raised to the third power and stored in the variable cube
    cube = i ** 3

    # each new value of the cube is appended to the list cubes
    cubes.append(cube)

# To write this code more concisely, omit the temporary variable cube and append each new value directly to the list:
# squares.append(value ** 3)

# Finally, when the loop has finished running, the list of cubes is printed
print("The cubes of numbers between 0 and 6 are:")
print(cubes)