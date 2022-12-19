'''
s="Itvedant-eclass"
print(s)
print(type(s))

sup=s.upper()
print(sup)

slow=sup.lower()
print(slow)
'''
#isalpha()
'''
This method check whether entire string contains alphabets.
If all string elements are alphabets then it return True
or it returns False.
'''

'''
s="itvedanteclass"

r=s.isalpha()
print(r)
'''
#isdigit():
'''
This method is used to check whether string elements are
digits i.e 0,1,2,3,...9
It returns True if string contains all digits.
It returns False if string contains other than digit.
'''
'''
s="12334567a"
r=s.isdigit()
print(r)
'''

#spliting
'''
when there is need to convert a string into list,split()
method is used.
syntax:
========
  str_variable.split('seprator')
  
'''
s="we are learning method in todaysclass"

print(s)
l=s.split()
#l=s.split(',')
print(l)
print(type(l))
