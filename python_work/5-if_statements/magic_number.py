# Numerical Comparisons
"""
Testing numerical values is pretty straightforward. For example, the following code checks whether a person is 18 years old:
>>> age = 18
>>> age == 18
True

You can also test to see if two numbers are not equal. For example, the following code prints a message if the given answer is not correct:
"""
answer = 17  

if answer != 42: #  The conditional test passes, because the value of answer (17) is not equal to 42.
    print("That is not the correct answer. Please try again!") # Because the test passes, the indented code block is executed:

"""
 You can include various mathematical comparisons in your conditional 
statements as well, such as less than, less than or equal to, greater than, and greater than or equal to:
>>> age = 19
>>> age < 21
True
>>> age <= 21
True
>>> age > 21
False
>>> age >= 21
False
Each mathematical comparison can be used as part of an if statement, 
which can help you detect the exact conditions of interest.
"""