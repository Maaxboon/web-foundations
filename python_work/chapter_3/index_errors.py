"""
One type of error is common to see when you’re working with lists for the first time. Let’s say you have a list with three items, and you ask for the fourth item:
"""

motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[3]) # This example results in an index error:

# Keep in mind that whenever you want to access the last item in a list you use the index -1. This will always work, even if your list has changed size since the last time you accessed it:
print(motorcycles[-1])