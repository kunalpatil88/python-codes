'''
code editor  ------print()-----> console(output screen)

If there is need to bring user input from output screen or
console to the code editor or to store in a variable, we need
input() function.

syntax:

   variable=input()

step1: Give message to user           => print()
step2: store that input into variable => var=input()
'''

print("enter the no:")
x=input()
#print(type(x))
a=float(x)
#print(type(a))
'''#print("value of x is:",x)
print("enter the scond no")
y=input()
z=x+y
print("addition of",x,"and",y,"is",z)
'''
print("enter second number:")
y=input()
b=float(y)
z=a+b
print("addition of",a,"and",b,"is",z)
