a=(input("Please enter the first time in four digits -HHMM:"))
b=(input("Please enter the second time in four digits -HHMM:"))
c = int(a[:2])*60 + int(a[2:])
d = int(b[:2])*60 + int(b[2:])
e = d - c
f= e//60
g = e%60
print("The difference between two given time is",f,"Hours",g,"Minutes")