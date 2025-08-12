"""
6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.
"""
people = {
    'maxtoshi' : {
        'nationality' : 'kenyan',
        'school' : 'african leadership university',
        'residence': 'kwananyinzira',
    },
    'ineza': {
        'nationality': 'rwandan',
        'school': 'university of rwanda',
        'residence': 'kacyiru',
    }
}

for person, person_info in people.items():
    print(f"{person.title()} is a {person_info['nationality'].title()} at the  {person_info['school'].title()} and resides at {person_info['residence'].title()}")
