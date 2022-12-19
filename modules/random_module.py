'''
random module
'''
import random as r
#random()
x=r.random()
print(x)

t=x*10000
print(t)

otp=round(t)
print("otp is send",otp)

otp=round(10000*r.random())
print("otp to be send:",otp)
