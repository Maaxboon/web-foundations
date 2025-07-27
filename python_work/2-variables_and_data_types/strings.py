# Strings
"""
A string is simply a series of characters. Anything inside quotes is considered a string in Python, and you can use single or double quotes around your strings like this: 
'This is a string'
"This is also a string"

This flexibility allows you to use quotes and apostrophes within your strings:
 'I told my friend, "Python is my favorite language!"'
 "The language 'Python' is named after Monty Python, not the snake."
 "One of Python's strengths is its diverse and supportive community."
"""

# Changing case in a string with methods: a method is an action that Python can perform on a piece of data
name = "ada lovelace"

print(name.title()) # title() displays each word in titlecase, where each word begins with a capital letter # prints: Ada Lovelace

print(name.upper()) # changes all characters to uppercase and prints ADA LOVELACE

print(name.lower()) # changes all characters to lowercase and prints ada lovelace

# combining or concatenating strings:  Python uses the plus symbol (+) to combine strings
first_name = "maxtoshi"
last_name = "okamoto"
full_name = first_name + " "+ last_name #  This method of combining strings is called concatenation
print("Hello, " + full_name.title() + "!") # prints: Hello, Maxtoshi Okamoto!

# You can use concatenation to compose a message and then store the entire message in a variable:
message = "Hello, " + full_name.title() + "!"
print(message)

# Adding Whitespace to Strings with Tabs or Newlines
"""
In programming, whitespace refers to any nonprinting character, such as spaces, tabs, and end-of-line symbols. You can use whitespace to organize your output so it’s easier for users to read.
"""
# To add a tab to your text, use the character combination \t as shown below
print("\t Python")

# To add a newline in a string, use the character combination \n:
print("Languages:\nPython\nC\nJavaScript")

# You can also combine tabs and newlines in a single string. The string "\n\t" tells Python to move to a new line, and start the next line with a tab. 
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Stripping whitespace
favourite_language = " Python "
print(favourite_language)
print(favourite_language.rstrip()) # strips whitespace from the right side
print(favourite_language.lstrip()) # strips whitespace from the left side
print(favourite_language.strip()) # strips whitespace from both sides

# Avoiding syntax errors with strings
message = "One of Python's strength, is it's diverse community"
print(message)