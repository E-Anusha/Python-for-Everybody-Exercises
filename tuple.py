'''
d = {'a':10, 'b':1, 'c':22}
print(d.items())
'''

#Sorted
d = {'d':10, 'b':1, 'c':22}
#t = sorted(d.items())
#print(t)
for k,v in sorted(d.items()):
    print(k,v)

'''
#Sort by values instead of key
c = {'a':10, 'b':1,'c':22}
tmp = list()
for k,v in c.items():
    tmp.append((v,k))
tmp = sorted(tmp, reverse=True)
print(tmp)
'''

c = {'d':10, 'b':1, 'c':22}
print(sorted([(v,k) for k,v in c.items()]))
#List comprehension creates a dynamic list. In this case,
#we make a list of reversed tuples and then sort it.