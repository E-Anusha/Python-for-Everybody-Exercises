'''
Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.
'''
'''
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter hourly rate:")
r = float(rate)
if  (h <= 40):
    gross_pay = h * r
else:
    h1 = h - 40
    pay1 = (h1) * (r * 1.5)
    gross_pay = (40 * r) + pay1
print(gross_pay)

----------------------------------------------------------
'''
'''
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter hourly rate:")
r = float(rate)
if  (h <= 40):
    gross_pay = h * r
else:
    gross_pay = (h *r) + ((h-40) * r * 0.5)
print(gross_pay)
-------------------------------------------
'''

hrs = input("Enter hours:")
rate = input("Enter rate per hour:")
try:
    fh = float(hrs)
    fr = float(rate)
except:
    print("Error, you need to enter the numericals only")
    quit()
print(fh,fr)
