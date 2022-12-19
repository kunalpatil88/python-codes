'''
raising  an exception
=====================
                                                                ------ Python
When ther is fault in runtime--Exception is raised--handled by-|
                                    by system                   ------ try..except

Till now exception is raised internally by system,
if there is need to raise an exception , then
use raise keyword to raise an exception.

exeception is raised with respect to certain condition.
syntax to raise exception
====
'''
x=int(input("Enter numerator:")) #x=9|x=9
y=int(input("Enter Denominator:")) #y=2|y=0

if y==0:
     raise ZeroDivisionError('denominator cannot be zero')
else:



    d=x/y#9/2=>4.5 | 9/0=> Exception is Raised| ZeroDivisionError
    print ("Division is:", d)
