'''
Calculator:Console based Application
=========
1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Exit

Enter your Choice:2

'''
while True:
    print("1. .Addition")
    print("2. Subtraction")
    print("3.Multiplication")
    print("4.,Division")
    print("5.Exit")
    print( )
    ch=int(input("Enter Your Choice"))#1,2,3,4,5 or other than 1-5

    if ch==1:
        x=int(input("enter first no:"))
        y=int(input("entr second no:"))
        z=x+y
        print("addition is:",z)
    elif ch==2:
        x=int(input("enter first no:"))
        y=int(input("entr second no:"))
        z=x-y
        print("substraction is:",z)
    elif ch==3:
        x=int(input("enter first no:"))
        y=int(input("entr second no:"))
        z=x*y
        print("multiplication is:",z)
    elif ch==4:
        x=int(input("enter first no:"))
        y=int(input("entr second no:"))
        z=x/y
        print("division is:",z)
    elif ch==5:
        print("exit from program,thank you for using services")
        break
    else:
        print("enter the valid no!!!!!:")
    
