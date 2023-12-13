counts = dict()
names = ['Anu', 'Raj', 'Ram', 'Paddu', 'Anu']
#print(type(names))

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)


#-------------

counts = dict()
names = ['Anu', 'Raj', 'Ram', 'Paddu', 'Anu']
for name in names:
    counts[name] = counts.get(name,0) + 1
print(counts)

#-------------

counts = dict()
print("Enter the statements to know the no. of repeatative words")
line = input()

words = line.split()
#print(words)

for word in words:
    counts[word] = counts.get(word,0) + 1

print(counts)

#---------------

sampledict = {'Anu':28,'Raj':31,'Ram':58,'Paddu':53}
for key in sampledict:
    print(key,sampledict[key])


