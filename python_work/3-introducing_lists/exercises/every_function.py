"""
3-10. Every Function: Think of something you could store in a list . For example, 
you could make a list of mountains, rivers, countries, cities, languages, or any
thing else you’d like . Write a program that creates a list containing these items 
and then uses each function introduced in this chapter at least once 
"""

cities = ['nairobi', 'kampala', 'kigali', 'durban', 'lagos']
print("\nHere is the original list of cities:")
print(cities)

# Sorted
print("\nHere is the temporary sorting of cities:")
print(sorted(cities))

print("\nHere is the original list of cities:")
print(cities)

# Reverse sorted
print("\nHere is the temporary reverse sorting of cities:")
print(sorted(cities, reverse=True))

# Permanent sort
cities.sort()
print("\nHere is the permanent sorting of cities:")
print(cities)

# Permanent reverse sort
cities.sort(reverse=True)
print("\nHere is the permanent reverse sorting of cities:")
print(cities)

# Insert
cities.insert(2, 'dodoma')
print(cities)

# pop
cities.pop()
print(cities)

# append
cities.append('addis')
print(cities)