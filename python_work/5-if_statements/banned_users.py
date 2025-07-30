# Checking Whether a Value Is Not in a List
"""
Other times, it’s important to know if a value does not appear in a list. You can use the keyword not in this situation. For example, consider a list of users who are banned from commenting in a forum. You can check whether a user has been banned before allowing that person to submit a comment:
"""
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

#  If the value of user is not in the list banned_users, Python returns True and executes the indented line.
if user not in banned_users:
    #  The user 'marie' is not in the list banned_users, so she sees a message inviting her to post a response:
    print(user.title() + ", you can post a response if you wish")
else:
    print(user.title() + ", you have been banned from posting a comment!")

# Boolean Expressions
"""
As you learn more about programming, you’ll hear the term Boolean expression at some point. A Boolean expression is just another name for a conditional test. A Boolean value is either True or False, just like the value of a conditional expression after it has been evaluated.
Boolean values are often used to keep track of certain conditions, such as whether a game is running or whether a user can edit certain content on a website:

game_active = True
can-edit = False

Boolean values provide an efficient way to track the state of a program or a particular condition that is important in your program.
"""