a=["January","February","March", "April","May","June", "July","August","September","October","November", "December"]
b=(input("Enter the date in the format 'MMDDYYYY' :\n"))
c = int(b[0:2])-1
print(a[c]+' '+ b[2:4]+',' + b[4:])
