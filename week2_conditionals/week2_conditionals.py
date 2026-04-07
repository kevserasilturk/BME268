"""
x=4
if x<5:
    print("x is less than 5")
if x>10:
    print("x is greater than 10")

x=20
if x<2:
    print("small")
elif x<10:
    print("medium")
else: 
    print("large")
print("all done")
"""

"""
astr="hello bob"
try:
    istr=int(astr)
except: 
    istr=-1
print("first",istr)


astr="123"
try:
    istr=int(astr)
except:
    istr=-1

print("second",istr)
"""

#rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours
hrs=input("Enter hours:")
try:
    hrs=float(hrs)
except:
    print("Error, please enter a numeric input.")

rate=input("Enter rate:")
try: 
    rate=float(rate)
except:
    print("Error, please enter a numeric input.")

if hrs>40:
    pay=40*rate+(hrs-40)*rate*1.5
else:
    pay=hrs*rate
print("Pay:",pay)




