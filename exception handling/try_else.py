'''
try....except and else
 else block is executed only when there is no exception.
 ...
 '''
try:
    x=int(input("Enter numerator:")) #x=9|x=9
    y=int(input("Enter Denominator:")) #y=2|y=0
    d=x/y#9/2=>4.5 | 9/0=> Exception is Raised| ZeroDivisionError
    print ("Division is:", d)
                                 
except Exception as x:
   #print ("Something Went Wrong !!!")
    print("Error:",x)
else:
     print("In the else block")
     print("division is:",d)




'''
else block is used to offload try block.
try block should always contains only those lines of code
in which there is chance of getting error.
code lines in which there is no chance of getting run time
error or exception must be in else block.
'''
