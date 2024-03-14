a=int(input())
lis=[]
m=True
n=0
stn=0
for x in range(a):
    b=int(input())
    lis.append(b)
lis.sort()
for y in range(a-1,-1,-1):
    if m==True:
        lis1=lis[y]
    m=False
    if lis[y]<lis1 :
         lis1=lis[y]
         n+=1
    if n==2:
         stay=lis1
         stn+=1
print(stay,stn)