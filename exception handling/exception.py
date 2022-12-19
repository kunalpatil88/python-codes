'''
Exception
=========

Error:These are the faults or mistake in the program.
There are two types of Errors
1)Compile time error
2)Runtime Error
Compile Time Error
=================
These errors are mainly due to mistake done in writing the
syntax of the code.

Run time Error
==============
The errors which occurs during program execution are called
as Run Time Error.
mainly due to User Input or importing module which is not there
at the location.
stag1: Error checking stage.
stag2: Code execution stage.
'''
#import arithmetic => run time error of modulenotfounderror
x=int(input("enter numerator:"))
y=int(input("enter denominator"))

d=x/y#9/2=4.5 | 9/0=> run time error =>exception
print("division is:",d)
