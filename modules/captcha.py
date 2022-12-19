import string as s
import random as r
alpha=s.ascii_letters
digit=s.digits
#print(alpha)
#print(digit)
alnum=alpha+digit
print(alnum)




'''
                       Alnum
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
position

captach would of 5 character.

step1:select random index value
step2:access character of that randomly selected index.
step3:concatenate with the string

'''
captcha=" "
for i in range(0,5):
    index=r.randrange(0,len(alnum))
   # print(index)
    #print(alnum[index])
    captcha=captcha+alnum[index]
    #print(captcha)
    #print("--------------------")
print(captcha)
