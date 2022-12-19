n1=int(input("enter first value :"))
n2=int(input("enter the second value:"))
def arithmetic(x,y):

   add=x+y
   sub=x-y
   mul=x*y
   div=x/y
   return add,sub,mul,div

a,b,c,d=arithmetic(n1,n2)

print("add:",a)
print("sub:",b)
print("mul:",c)
print("div:",d)
