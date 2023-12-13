'''
Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count,and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.
'''
'''
count = 0
total = 0
while True:
    num = input('Enter a number:')
    try:
        n = float(num)
        count = count + 1 
    except:
        if num == 'done':
            break
        else:
            print("Enter numericals only or Enter 'Done' to stop")
            continue
    total = total + n
print("The total of the entered numbers:",total)
print("The count of the entered numbers:",count)
while count != 0:
    print("The average of the entered numbers:",(total/count))
    break
'''
'''
num = 0
tot = 0.0
while True:
    sval = input('Enter a number:')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    num = num+1
    tot = tot+1
''' 

'''
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
'''
'''
largest = None
smallest = None
while True:
    num = input('Enter a number:')
   if num == 'done':
   #     break
    try:
        fval = float(num)
        if largest is None:
            largest = num
        if smallest is None:
            smallest = num
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
        continue
    except:
        if num == 'done':
            break
        else:
            print('Invalid input')
            continue
print("Maximum is", largest)
print("Minimum is", smallest)
'''

count = 0
largest = None
smallest = None

while True:
    num = input('Enter a number:')

    if num == 'done':
        break
        
    try:
        num = float(num)
        
    except:
        print('Invalid input')
        continue
    
    if count == 0:
        smallest = num
        largest = num
    elif num > largest:
        largest = num
    elif num < smallest:
        smallest = num
    
    count = count + 1

print("Maximum is", int(largest))
print("Minimum is", int(smallest))
   






