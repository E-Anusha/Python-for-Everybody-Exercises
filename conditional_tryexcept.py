'''
astr = input()
try:
    istr = int(astr) #alphabetical string can't be converted to integer.hence, exception block.
except:
    istr = 404
print("Hey there, the given string can't be converted into integer, hence replaced by integer using exception", istr)

----------------------------------------------
astr = "12345"
try:
    istr = int(astr) #alphabetical string can't be converted to integer.hence, exception block.
except:
    istr = -2
print("Hey there, the given string can't be converted into integer, hence replaced by integer using exception", istr)
'''
'''
-------------------------------------------------
astr = input()
print(type(astr))
istr = int(astr)
print(istr)
print(type(istr))
---------------------------------------------------
'''
givenstr = input("enter a number:")
try:
    istr = int(givenstr)
except:
    istr = 101

if istr > 0:
    print("done",istr)
elif istr < 0:
    print("less than the zero",istr)
else:
    print("conversion didn't happen, as it is other than the digits in the decimal system")
    
