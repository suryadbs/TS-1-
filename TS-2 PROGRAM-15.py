def angle(n):
    if n<3:
        print('\t\tIt is Not a Polygon')
    else:
        a=(n-2)*180
        print('\tAngle Sum of',n,'Side Polygon is :',a)
a=int(input('\tEnter Number of sides of Polygon :'))
print()
angle(a)
print()
