def second(a):
    b=a*24 * 60*60
    print("Number of seconds in the entered year is :", b)
a = int(input("Enter a year: "))
if (a % 400 == 0) and (a % 100 == 0):
    print(a," is a leap year")
    second(366)
elif (a % 4 ==0) and (a % 100 != 0):
    print(a,"is a leap year")
    second(366)
else:
    print(a,"is not a leap year")
    second(365)