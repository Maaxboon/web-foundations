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
 You can include various mathematical comparisons in your conditional statements as well, such as less than, less than or equal to, greater than, and greater than or equal to:
>>> age = 19
>>> age < 21
True
>>> age <= 21
True
>>> age > 21
False
>>> age >= 21
False
Each mathematical comparison can be used as part of an if statement, which can help you detect the exact conditions of interest.
"""

#  Checking Multiple Conditions
"""
You may want to check multiple conditions at the same time. For example, sometimes you might need two conditions to be True to take an action. Other 
times you might be satisfied with just one condition being True. The keywords and and or can help you in these situations.
"""
# Using and to Check Multiple Conditions
"""
To check whether two conditions are both True simultaneously, use the keyword and to combine the two conditional tests; if each test passes, the over all expression evaluates to True. If either test fails or if both tests fail, the expression evaluates to False.
For example, you can check whether two people are both over 21 using the following test:
#  we define two ages, age_0 and age_1
>>> age_0 = 22
>>> age_1 = 18
# we check whether both ages are 21 or older
# The test on the left passes, but the test on the right fails
>>> age_0 >= 21 and age_1 >= 21
# so the overall conditional expression evaluates to False
False
#  we change age_1 to 22.  
>>> age_1 = 22
The value of age_1 is now greater than 21, so both individual tests pass 
>>> age _0 >= 21 and age_1 >= 21
causing the overall conditional expression to evaluate as True.
True

To improve readability, you can use parentheses around the individual 
tests, but they are not required. If you use parentheses, your test would look like this:
(age_0 >= 21) and (age_1 >= 21)
"""
#  Using or to Check Multiple Conditions
"""
The keyword or allows you to check multiple conditions as well, but it passes when either or both of the individual tests pass. An or expression fails only when both individual tests fail.
Let’s consider two ages again, but this time we’ll look for only one person to be over 21:
# We start with two age variables again
>>> age_0 = 22
>>> age_1 = 18
#  The test for age_0 at v passes
>>> age_0 >= 21 or age_1 >= 21
# the overall expression evaluates to True
True

#  We then lower age_0 to 18
>>> age_0 = 18
# both tests now fail 
>>> age_0 >= 21 or age_1 >= 21
# the overall expression evaluates to False.
False
"""
