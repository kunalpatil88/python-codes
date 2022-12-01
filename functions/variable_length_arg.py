'''

variable length argument
========================

variable:changing

length:number of argument


'''
def addition(*x):
   #print(x)
   #print(type(x))
    sum=0
    for i in x:
        #print(i)
        sum=sum+i
    print("summetion is",sum)
    
addition(20,30)
addition(20,30,40)
addition(20)
