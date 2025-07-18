# 2-3. Personal Message: Store a person’s name in a variable, and print a message to that person . Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
name = "Maxtoshi" # stores the value Maxtoshi in a variable name 
message = "Hello " + name + ", " + "would you like to learn some Python today?" # store the value of message
print(message)

# 2-4. Name Cases: Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase .
first_name = "maxtoshi"
print(first_name.lower()) # prints first_name in lowercase: maxtoshi
print(first_name.upper()) # prints first_name in uppercase: MAXTOSHI
print(first_name.title()) # capitalizes the first character of first_name: Maxtoshi


"""
2-5. Famous Quote: Find a quote from a famous person you admire . Print the quote and the name of its author . Your output should look something like the following, including the quotation marks:Albert Einstein once said, “A person who never made a mistake never tried anything new.”
"""
print('James Gosling once said, "I am not a great programmer. I am just a good programmer with great habits"')


# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time store the famous person’s name in a variable called famous_person . Then compose your message and store it in a new variable called message . Print your message .
famous_person = "James Gosling"
message = famous_person + 'once said, ' + '"I am not a great programmer. I am just a good programmer with great habits."'
print(message)

"""
2-7. Stripping Names: Store a person’s name, and include some whitespace characters at the beginning and end of the name . Make sure you use each character combination, "\t" and "\n", at least once .
Print the name once, so the whitespace around the name is displayed . 
Then print the name using each of the three stripping functions, lstrip(), 
rstrip(), and strip()
"""

last_name = " Okamoto "
print(last_name)
print("\n" + last_name.lstrip())
print("\t" + last_name.rstrip())
print(last_name.strip())