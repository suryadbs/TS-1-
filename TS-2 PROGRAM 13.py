print('*'*40)
def min(a,b):
    if a==b:
        print('Once Digits are Equal')
    elif a>b:
        print('Once Digit of Second Number is Minimum')
    else:
        print('Once Digit of first Number is Minimum')
x=input('\t\t Enter Number 1 :')
y=input('\t\t Enter Number 2 :')
print()
min(x[-1],y[-1])
print()
print('*'*40)