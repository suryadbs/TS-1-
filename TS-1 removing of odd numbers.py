def list(l):
    a = []
    for i in range(0,len(l)):
        if l[i] %2 == 0:
            a.append(l[i])
    return a
b=[]
for i in range(0,10):
    b.append(i+1)
print("The given list of elements are:\n", b)
print()
c=list(b)
print ("The new list without odd numbers are:\n", c)