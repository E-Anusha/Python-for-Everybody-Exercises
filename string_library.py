'''
greet = 'Hello Bob'
zap = greet.lower()
paz = greet.upper()
type(greet)
dir(greet)#gives all the valid function
rpl = greet.replace('Bob','Anu')
rpl1 = greet.replace('o','a')
print(zap)
print(paz)
print(rpl1)
print(rpl)
'''

#Stripping whitespaces
'''
#greet1 = 'a    Hello Bob  b'
greet1 = '    Hello Bob  '
print(greet1.lstrip())
print(greet1.rstrip())
print(greet1.strip())
'''

#Prefixes
'''
line = 'PLease have a nice day'
print(line.startswith('Please'))
print(line.startswith('PLease'))
print(line.startswith('p'))
'''

#Parsing and Extracting
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ',atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)


