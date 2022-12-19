'''
When there is need to preserve old data or new data must be
added at the end of the old data use append mode.

'''
fp=open('data.txt','a')
#d="this is first line in the file"
d=input("enter the value:")
data=d+"\n"
fp.write(data)
fp.close()
