
abc = 'With three words'
stuff = abc.split()
#print(stuff)
for w in stuff:
    print(w)

#-----------------

'''
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    words = line.split()
    print(words[2])
    
'''


'''
##DoubleSplit
txt = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"

words = txt.split()
email = words[1]
'''
'''
friends = [ 'Joseph', 'Glenn', 'Sally' ]
friends.sort()
print(friends[0])
'''