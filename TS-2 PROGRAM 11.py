print('# '*10)
import random as r
def ran(a,b):
    return r.randint(a,b)
a=int(input(' Enter Number 1 :'))
b=int(input(' Enter Number 2 :'))
print()
for i in range(1,4):
    print('\t\t',ran(a,b))
print('\n','# '*10)