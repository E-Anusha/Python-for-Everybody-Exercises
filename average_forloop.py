counter = 0
total = 0
print("The counter and the total is assigned to zero","counter:",counter,"total:",total)
for i in [8,3,6,8.5,7.8,2.5,7,-2,-9,0,-3]:
    counter = counter + 1
    total = total + i
    print("During the iteration:","counter:",counter,"total:",total,"iteration variable",i)
print("After the iteration:","counter:",counter,"total:",total)
print("The average is:", (total/counter))