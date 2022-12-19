
'''

                    datetime
                       |
            --------------------------
           |           |              |
         date         time         datetime  1 level
                                      |
                                       -year()
                                      |
                                       -month()  2nd level
                                      |
                                       - day()

'''



#create datetime

import datetime 
'''
date=datetime.datetime(2022,11,21)
print(date)

date2=datetime.datetime(2022,11,21,20,25,45)
print(date2)
'''

#to extract system date and time use now() method
#sysdt=datetime.datetime.now()
sysdt=datetime.datetime.today()
print(sysdt)

y=sysdt.year
print(y)
m=sysdt.month
print(m)
d=sysdt.day
print(d)
h=sysdt.hour
print(h)
minu=sysdt.minute
print(minu)
sec=sysdt.second
print(sec)
