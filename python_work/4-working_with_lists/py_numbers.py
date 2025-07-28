"""
Using the range() Function
Python’s range() function makes it easy to generate a series of numbers. 
For example, you can use the range() function to print a series of numbers like this:
"""
for value in range(1,5):
    print(value) 
"""
although this code looks like it should print the numbers from 1 to 5, it doesn’t print the number 5:
In this example, range() prints only the numbers 1 through 4. This is another result of the off-by-one behavior you’ll see often in programming languages. The range() function causes Python to start counting at the first value you give it, and it stops when it reaches the second value you provide. 
Because it stops at that second value, the output never contains the end value, which would have been 5 in this case.To print the numbers from 1 to 5, you would use range(1,6):
"""

for value in range(1,6):
    print(value) #  This time the output starts at 1 and ends at 5: