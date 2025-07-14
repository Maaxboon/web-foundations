# Variables: variables hold values
message = "Hello Python World!" # The variable message holds the value: "Hello Python world!"
print(message) # Prints the value of message

message = "Hello Python Crash Course World!" # The variable message has been changed to the value: "Hello Python Crash Course World!"
print(message) # You can change the value of a variable in your program at any time, and Python will always keep track of its current value

# Naming and using variables
"""
Variable names can contain only letters, numbers, and underscores. They can start with a letter or an underscore, but not with a number. For instance, you can call a variable message_1 but not 1_message.
Spaces are not allowed in variable names, but underscores can be used to separate words in variable names. For example greeting_message works, but greeting message will cause errors.
Avoid using Python keywords and function names as variable names; that is, do not use words that Python has reserved for a particular programmatic purpose, such as the word print. 
Variable names should be short but descriptive. For example, name is better than n, student_name is better than s_n, and name_length is better than length_of_persons_name.
Be careful when using the lowercase letter l and the uppercase letter O because they could be confused with the numbers 1 and 0.
"""