a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
c=input("enter the operation symbol: ")
if(c=='+'):
    print(a+b)
elif(c=='-'):
    print(a-b)
elif(c=='*'):
    print(a*b)
elif(c=='/'):
    print(a/b)
elif(c=='%'):
    print(a%b)
else:
    print("invalid operation")
