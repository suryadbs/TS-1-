a=eval(input("Enter a list: "))
b=0
for i in range (len(a)) :
  if len(a[i])>b :
    word=a[i]
    b=len(a[i])
print("The longestword in the list is :",word)