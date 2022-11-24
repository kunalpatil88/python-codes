
'''
Check whether string entered by user is palindrome or not.

            N I T I N
            -------->
            <--------

    if original string == reversed string  => It is palindrome
algo
===
step1:start
step2:reversed string entered by user.
step3:check reversed and original string
step4:if both are equal then its palindrome otherwise not.

reversed  ===>  [::-1]
'''
org=input("enter the string:")
rev=org[::-1]
print("orignal value",org)
print("reversed value",rev)
if org==rev:
    print("string is palindrome")
else:
    print("it is not palindrome")
