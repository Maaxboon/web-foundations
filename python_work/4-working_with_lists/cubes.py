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

# List comprehension: Allows us to generate the same listof cubes in just one line
cubes = [value **3 for value in range(0,6)]
print(cubes)