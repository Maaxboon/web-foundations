# The while Loop in Action
"""
You can use a while loop to count up through a series of numbers. For example, the following while loop counts from 1 to 5:
"""
#  we start counting from 1 by setting the value of current_number to 1
current_number = 1
"""
Because 1 is less than 5, Python prints 1 and then adds 1, making the current number 2. Because 2 is less than 5, Python prints 2 and adds 1 again, making the current number 3, and so on. Once the value of current_number is greater than 5, the loop stops running and the program ends
"""
while current_number <= 5:
    print(current_number)
    current_number += 1