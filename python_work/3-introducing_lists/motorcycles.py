#  Changing, adding, and removing elements
# Modifying Elements in a List
"""
The syntax for modifying an element is similar to the syntax for accessing an element in a list. To change an element, use the name of the list followed by the index of the element you want to change, and then provide the new value you want that item to have.
"""
# Initial list of motorcycles
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) 

# changing the value of honda
motorcycles[0] = 'ducati'
print(motorcycles) # ['ducati', 'yamaha', 'suzuki']

# Adding elements to a list
# Appending Elements to the end of a list
"""
The simplest way to add a new element to a list is to append the item to the 
list. When you append an item to a list, the new element is added to the end 
of the list. Using the same list we had in the previous example, we’ll add the 
new element 'ducati' to the end of the list:
"""

# adding bmw to the end of the list
motorcycles.append('bmw')
print(motorcycles) # ['ducati', 'yamaha', 'suzuki', 'bmw']

"""
The append() method makes it easy to build lists dynamically. For 
example, you can start with an empty list and then add items to the list 
using a series of append() statements. Using an empty list, let’s add the ele
ments 'ALU', 'ALA', and 'ALCHE' to the list:
"""

ALG = []
ALG.append("ALA")
print(ALG) # ['ALA']

ALG.append("ALC")
print(ALG) # ['ALA', 'ALC']

ALG.append("ALU")
print(ALG) # ['ALA', 'ALC', 'ALU']

# Inserting elements into a list
"""
You can add a new element at any position in your list by using the insert() 
method. You do this by specifying the index of the new element and the 
value of the new item.
"""
ALG.append("ALCHE")
print(ALG) # ['ALA', 'ALC', 'ALU', 'ALCHE']

ALG.insert(3, 'ALX')
print(ALG) # ['ALA', 'ALC', 'ALU', 'ALX', 'ALCHE']

# Removing elements from a list
# removing an Item Using the del Statement
"""
 If you know the position of the item you want to remove from a list, you can 
use the del statement. 
"""
del motorcycles[1]
print(motorcycles)

# removing an Item Using the pop() Method
"""
Sometimes you’ll want to use the value of an item after you remove it from a 
list. For example, you might want to get the x and y position of an alien that 
was just shot down, so you can draw an explosion at that position. In a web 
application, you might want to remove a user from a list of active members 
and then add that user to a list of inactive members.
The pop() method removes the last item in a list, but it lets you work 
with that item after removing it. The term pop comes from thinking of a 
list as a stack of items and popping one item off the top of the stack. In 
this analogy, the top of a stack corresponds to the end of a list.
"""

# Let’s pop a county from the list of counties:
counties = ['Siaya', 'Kisumu', 'Homabay', 'Migori', 'Kisii', 'Nyamira']
print(counties)
popped_county = counties.pop()
print(counties)
print(popped_county)

last_removed = counties.pop()
print("The last county to be removed was " + last_removed + " county." )

# Popping items from any position in a list
members = ['Kambai', 'Ngugi', 'Kuria', 'Wanyama', 'Okoth']
non_member = members.pop(0)
print("The non member in the team was mzee " + non_member)

# Removing an item  by value
"""
Sometimes you won’t know the position of the value you want to remove 
from a list. If you only know the value of the item you want to remove, you 
can use the remove() method.
"""

cities = ['nairobi', 'kigali', 'kampala', 'lagos', 'pretoria']
print(cities)
cities.remove('lagos')
print(cities)

not_in_east_africa = 'pretoria'
cities.remove(not_in_east_africa)
print(cities)
print(not_in_east_africa.title() + " is not in East Africa.")