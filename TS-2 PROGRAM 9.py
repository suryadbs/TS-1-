print('*'*35)
'''Void Function'''
def rup(d):
    print(d,'$ is equal to',d*76,'Rupees')
'''Non Void Function'''
def Rup(d):
    return d*76
a=int(input(' Enter the Amount in Dollers :'))
print('*'*35)
print('\n\t\tCalling Void Function\n')
rup(a)
print()
print('*'*35)
print('\t  Calling Non Void Function\n')
print(a,'$ is equal to',Rup(a),'Rupees\n')
print('*'*35)