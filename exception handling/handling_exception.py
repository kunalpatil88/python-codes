'''
handling any exception with exception parent class.
'''

try:
    x=int(input("enter numerator:"))
    y=int(input("enter denominator:"))
    d=x/y
    print("division is:",d)
except Exception as e:
   # print("somting went wrong!!!!")
     print("error:",e)
     
