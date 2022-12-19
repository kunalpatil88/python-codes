'''
try...except...finally

finally block is executed in both situation
1)If there is exception.
2)If there is no exception.
'''

try:
    x=int(input("enter numerator:"))
    y=int(input("enter denominator:"))
    d=x/y
    print("division is:",d)
except Exception as e:
   # print("somting went wrong!!!!")
     print("error:",e)
finally:
    print("inside finaly block")


'''
Whenever a transation of inserting record, retrieve records
update record and delete record with the database is
completed, it is a good practice to close connection of
your code with database, so that data is secured.

      python ---Connection----> Database [to perform operations]

And even if exception arises, then connection to the database
must be closed.

'''
     
