'''
String
======
1)String is a collection of characters.
2)They are enclosed in single quote or double quote or
  triple quoted.
3)String are immutable i.e once string is formed it
  cannot be changed.[No addition,No replace and No delete]
'''

x="itvedant-eclass"
'''
#x=this is comment
print(x)
print(type(x))

#len() is used for calculate the no of charector in string

n=len(x)
print("total no of char",n)


#indexing
Need: To process string charecter by character , there is need to
access charecter in the string. indexing helps you to access
character in the string.
there are two types of indexing'
1)positive indexing
2)Negativeindexing


positive indexing

                   I t v e d a n t - e c  l  a  s  s
                   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
               


print(x[5])
print(x[-5])
'''

#slicing
'''
need of slicing:
================
if there is need to extract partial part of the sring from
entire string, then use slicing

1) to revrse string
'''
'''
#x1=x[2:8:1]
#x1=x[10:15:1]
#x1=x[2:12:2]
#x1=x[2:8:]
#x1=x[:8:]
#x1=x[::]
#print(x1)

step=> negative
#x1=x[14:8:-1]
#print(x1)

for i in range(0,len(x),1):
 print(x[i])

 #without index
print("without index")
for i in x:
  print(i)

print(x[2])
x[2]-"o" #item assignment
print(x[2])
  '''
