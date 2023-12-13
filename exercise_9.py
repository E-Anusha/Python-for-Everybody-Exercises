'''
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
cwen@iupui.edu 5
'''

name = input("Enter the input file:")
handle = open(name)

count = dict()

for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    linewords = line.split()
    mail = linewords[1:2]
    #print(mail)
    for i in mail:
        count[i] = count.get(i,0)+1

pro_committer = None
pro_count = None
for mail_id,large_count in count.items():
    if pro_count is None or large_count > pro_count:
        pro_committer = mail_id
        pro_count = large_count
        
print(pro_committer, pro_count)
