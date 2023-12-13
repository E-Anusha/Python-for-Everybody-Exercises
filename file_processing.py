#fhand = open("C:\\Users\\anush\\Desktop\\py4e\\patentsample.txt")
'''
count = 0
for line in fhand:
    count = count+1
print('Line Count:' , count)
'''

'''
flen = fhand.read()
print(len(flen))
print(flen[:20])
'''


'''
for line in fhand:
    line = line.rstrip()
    #if line.startswith('From:'):
    #    print(line)
    if not line.startswith('From:'):
        continue
    print(line)
'''

fname = input('Enter the file name:')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
    
count = 0
for line in fhand:
    if line.startswith('The'):
        count = count+1
print('There were',count,'line')