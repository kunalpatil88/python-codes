'''
list
====
1)List is collection of dissimialr datatype elements.
2)Element in list are enclosed in square brackets.
3)List is mutable.[Once defined they can be changed.]
'''
l=[10,89.7,-3,45.6,'itvedant']
print(l)
print(type(l))

#length
n=len(l)
print("total no of element in list:",n)

#indexing
'''
                       l
                       
          [10,89.7,-3,45.6,'Itvedant']
           0   1    2  3       4
           -5  -4  -3  -2      -1
           
Accessing list element
    syntax:

        list_variable[index_value]
'''
#print(l[3])
#print(l[-4])

#slicing
'''
l1=l[1:4:1]
print(l1)

lrev=l[::-1]
print(lrev)

#for loop over list
print("with index")
for i in range(0,len(l),1):
    print(l[i])
print("without index")
for i in l:
    print(i)
 '''   '''
There are two methods or function to add
element in the list.
1)append():
   This function or method is used to add element at the
   end of the list.
   syntax:
          list_variable.append(element)'''
l.append(24.5)
print(l)
l.append('eclass')
print(l)
'''
2)insert():
  This function or method is used to add element at
  specific index position

  list_variable.insert(index_pos,value)
'''



  #delete or remove list elements.
'''
pop(): This is used to delete last elements.

pop(index):This remove specific element whose index is
mentioned in the pop() method.

'''
'''

l.insert(3,50)
print(l)
#update()
l[4]="itvedant-eclass"
print(l)
'''
'''
syntax:

  list_variable[index_pos]=value
'''      

l.pop()
print(l)


l.pop(2)
print(l)
#del :keyword used to delete entire list at once

del l
print(l)
