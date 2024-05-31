print("--CALCULATOR--")
print("C () % /\n7 8 9  *\n4 5 6  -\n1 2 3  +\n")

while True:
    print("Enter two numbers to perform the operation: ")
    a=int(input())
    b=int(input())
    print("Options available are:\n1 for Addition\n2 for Subtraction\n3 for Multiplication\n4 for Division\n5 for Remainder\n6 for Clear")
    print("Enter your choice: ")
    n=int(input())
    while n>6 or n<1:
        print("Enter valid choice please--")
    if(n==1):
        res=a+b
        print("Addition of",a,"and",b,"is",res)
    elif(n==2):
        res=a-b
        print("Subtraction of",a,"and",b,"is",res)
    elif(n==3):
        res=a*b
        print("Multiplication of",a,"and",b,"is",res)
    elif(n==4):
        res=a/b
        print("Division of",a,"and",b,"is",res)
    elif(n==5):
        res=a%b
        print("Remainder when",a,"is divided by",b,"is",res)
    elif(n==6):
        continue
    
    print("Thanks for using our calculator")
    break
