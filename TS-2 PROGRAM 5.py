print('$'*50,'\n')
n1=0
n2=1
b=[0,1]
for i in range(7):
   c=n1+n2
   n1=n2
   n2=c
   b.append(c)
print('   Tuple of First 9 terms of Fibonaccy Series :','\n')
print('\t',tuple(b),'\n')
print('$'*50)