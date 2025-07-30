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