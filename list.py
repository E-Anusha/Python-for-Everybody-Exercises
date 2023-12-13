#friends = ['Joseph', 'Glenn', 'Sally']

'''
for friend in friends:
    print('Happy New Year:', friend)
'''


'''
for i in range(len(friends)):
    print('Happy New Year:', friends[i])
'''

#---------------------
'''
stuff = list()
stuff.append('book')
stuff.append('Anu')
stuff.append(99)
print(stuff)
'''
#--------------------

numlist = list()
while True:
    i = input('Enter the list values:')
    if i == 'done':
        break
    value = float(i)
    numlist.append(value)
    
average = (sum(numlist))/len(numlist)
print('Average is', average)