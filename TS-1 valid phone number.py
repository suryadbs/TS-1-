p=input("Enter a phone number:")
if len(p)==12 and p[3]=='-' and p[7] == '-':
    if( p[:3]+p[4:7]+p[8:]).isdigit():
         print("The Phone number is valid")
    else:
         print("The Phone number is not valid")
else:
    print("The Phone number is not valid")