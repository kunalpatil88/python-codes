'''g
handling Multiple Exception
==========================

try:

    code to be insepected for Exception
    or
    code in which there is chance of
    getting execption.

except ExceptionName1:

   except block to given msg.
except ExceptionName2:
   except block to given msg.
.
.
.
except ExceptionNamen:
  except block to given msg
'''
#try:
x=int(input("enter numerator:"));
y=int(input("enter denominator:"));

d=x/y
print("division is:",d)
#except ZeroDivisionError:
print("denominator cannot be zero, please enter no other")
#except ValueError:
    #print("Enter proper digit for numeric or denominator")
