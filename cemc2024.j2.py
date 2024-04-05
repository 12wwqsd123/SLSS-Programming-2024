a=int(input())
number=[]
m=True
for x in range(6):
    b=input()
    if m==True and a<=int(b):
        #print(a)
        break
    m=False
    number.append(b)
for y in number:
    if a>int(y):
        a+=int(y)   
    else:
        break
print(a)