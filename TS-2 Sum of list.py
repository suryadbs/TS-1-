print('='*60,'\n')
print('\t\t\t\tEnter 2 List of same size\n')
print('='*60,'\n')
a=eval(input('Enter List 1 :'))
b=eval(input('Enter List 2 :'))
c=[]
for i in range(len(a)):
   c.append(a[i]+b[i])
print()
print('Sum of Corresponding Elements of List :',c,'\n')
print('='*60)