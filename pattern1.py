# n is the input for number of lines to be printed with the desired pattern
n = int(input("Enter the number of lines: "))

# Rectangle-shaped pattern program starts here
# i denotes the row index and j denotes the column index
# end='' prevents moving to a new line after each print statement
for i in range(n):
    for j in range(n):
        print('*', end = '')
    # Print a new line after each row is completed
    print()

'''
Output:
(if n = 3)

***
***
***

'''
