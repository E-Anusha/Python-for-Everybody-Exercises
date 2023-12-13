'''
friends = ['Joseph', 'Glenn' , 'Sally']
for f in friends:
    print('Happy New Year:' , f)
print('Done!')
---------------------
'''

'''
large_num = -1
print("Before the iterataion, the largest number is:", large_num)
for i in [89,80,24,8,2,4,99,0,1,-1,-3,-6]:
    if i >= large_num:
        large_num = i
    print("The iteration is:", large_num, i)
print("After the iteration, the largest number is:", large_num)
---------------------
'''
'''
#Flaw program as we declared the small_num
small_num = -1
print("Before the iteration smallest number is:",small_num)
for i in [8,3,2,5,7,9,4,-6,7]:
    if i <= small_num:
        small_num = i
    print("The smallest number so far:",small_num,"The iteration variable is:",i)
print("After the iteration smallest number is:",small_num)
----------------------
'''

#Integer operations can't be performed on None
small_num = None
print("Before the iteration smallest number is set to None")
for i in [8,3,2,5,7,9,4,-6,7]:
    if small_num is None:
        small_num = i
    elif i < small_num:
        small_num = i
    print("The smallest number so far:",small_num,"The iteration variable is:",i)
print("After the iteration smallest number is:",small_num)



      

'''
counter = 0
print("Before the iteration, the counter is:",counter)
for i in [80,4,7,9,2,1,78.89,3]:
    counter = counter + 1
    print(counter,i)
print("After the iteration, the counter is:",counter)
---------------------
'''
'''
found = False
print("Before", found)
for value in [9,67,3,8,29,-9.3,5.67,3]:
    if value == 3:
        found = True
    print(value,found)
print("After",found)
'''