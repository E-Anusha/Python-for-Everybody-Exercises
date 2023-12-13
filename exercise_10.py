'''
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
Desired Output
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
'''

name = input('Enter the file name:')

'''
if len(name)<1:
    name = 'C:\\Users\\anush\\Desktop\\py4e\\mbox-short.txt'
'''  

handle = open(name)

counts = dict()

lst = []

for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    linewords = line.split()
    maildata = linewords[0:10]
    #print(maildata)
    time = maildata[5].split(':')
    #print(time[0])
    hour = time[0]
    counts[hour] = counts.get(hour,0) + 1

print(counts)
        
'''
        cursor = time.find(":")
        hour = time[cursor-1:cursor]
        #print(hour)
        for h in hour:
            counts[hour] = counts.get(hour,0) + 1
'''
#print(counts)
for key,value in (counts.items()):
    lst.append((key,value))
    
lst.sort()

for k,v in lst:
    print(k,v)

