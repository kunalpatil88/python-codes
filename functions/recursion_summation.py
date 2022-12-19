'''
Summation of 1 to n using Recursion.
n=5
1+2+3+4+5=15
'''

num=int(input("enter last erm in the series:"))
def summation(n):
    if n==1:
        return 1
    r=n+summation(n-1)
    return r
res=summation(num)
print("summation is:",res)
