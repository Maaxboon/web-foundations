# To reverse the original order of a list, you can use the reverse() method. 
"""
If we originally stored the list of cars in chronological order according to when we owned them, we could easily rearrange the list into reverse chronological order:
"""
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars) # Notice that reverse() doesn’t sort backward alphabetically; it simply reverses the order of the list: