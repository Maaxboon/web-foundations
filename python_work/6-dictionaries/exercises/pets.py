"""
6-8. Pets: Make several dictionaries, where the name of each dictionary is the name of a pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do print everything you know about each pet.
"""
ziggy = {
    'type' : 'cat',
    'owner' : 'flk',
}

popsy = {
    'type' : 'dog',
    'owner' : 'daraja',
}

pets = [ziggy, popsy]

for pet in pets:
    print(f"Pet type: {pet['type'].title()}")
    print(f"Pet owner: {pet['owner'].title()}")
    print("------------------------")