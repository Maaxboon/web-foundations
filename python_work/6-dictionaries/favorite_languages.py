# A Dictionary of Similar Objects
favorite_languages = {
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python',
    }

# print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title())
print("----------------------------------------------------------\n")

# Looping Through All the Keys in a Dictionary
"""
The keys() method is useful when you don’t need to work with all of the values in a dictionary. Let’s loop through the favorite_languages dictionary and print the names of everyone who took the poll:
"""
#  tells Python to pull all the keys from the dictionary favorite_languages and store them one at a time in the variable name.
for name in favorite_languages.keys():
    print(name.title())
print("----------------------------------------------------------\n")

#  Looping through the keys is actually the default behavior when looping through a dictionary, so this code would have exactly the same output if you wrote . . . 
for name in favorite_languages:
    print(name.title())
print("----------------------------------------------------------\n")
#  rather than . . .
for name in favorite_languages.keys():
    print(name.title())
print("----------------------------------------------------------\n")

"""
You can access the value associated with any key you care about inside the loop by using the current key. Let’s print a message to a couple of friends about the languages they chose. We’ll loop through the names in the dictionary as we did previously, but when the name matches one of our friends, we’ll display a message about their favorite language:
"""
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")
print("----------------------------------------------------------\n")

"""
You can also use the keys() method to find out if a particular person was polled. This time, let’s find out if Erin took the poll:
"""
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
print("----------------------------------------------------------\n")

# Looping Through a Dictionary's Key's in order
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll!")
print("----------------------------------------------------------\n")

# Looping Through All Values in a Dictionary
"""
If you are primarily interested in the values that a dictionary contains, you can use the values() method to return a list of values without any keys. 
For example, say we simply want a list of all languages chosen in our programming language poll without the name of the person who chose each language:
"""
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
print("-----------------------------------------------------\n")

"""
This approach pulls all the values from the dictionary without checking for repeats. That might work fine with a small number of values, but in a poll with a large number of respondents, this would result in a very repetitive list. To see each language chosen without repetition, we can use a set. 
A set is similar to a list except that each item in the set must be unique:
"""
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())