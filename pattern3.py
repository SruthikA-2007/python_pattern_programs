# n is the input for number of lines to be printed with the desired pattern
n = int(input("Enter the number of lines: "))

# Inverted right triangle pattern program starts here
# i denotes the row index and j denotes the column index
# end='' prevents moving to a new line after each print statement
for i in range(0,n):
    for j in range(n,i,-1):
        print('*', end = '')
    # Print a new line after each row is completed
    print()


# This is another way of printing inverted right triangle
for i in range(0,n):
    for j in range(0,n-i):
        print('*', end = '')
    print()

'''
Output:
(if n = 3)

***
**
*

'''