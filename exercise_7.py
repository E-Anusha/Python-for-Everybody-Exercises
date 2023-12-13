'''
7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt
'''

'''
fname = input("Enter the file name:")
fh = open(fname)
fstore = fh.read()
fstore.rstrip()
print(fstore.upper())
'''


'''
fname = input("Enter the file name:")
fh = open(fname)
#fstore=fh.read()
for line in fh:
    line = line.rstrip()
    print(line.upper())
'''

'''
------------------------
7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name. 
Average spam confidence: 0.7507185185185187
'''

fname = input("Enter the file name:")
fo = open(fname)
'''
count = 0
val = 0.0
for line in fo:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count+1
        pos = line.find(':')
        val = val + float(line[(pos+1):])
print("Average spam confidence:",float(val/count))

'''

fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    print(line)
print("Done")