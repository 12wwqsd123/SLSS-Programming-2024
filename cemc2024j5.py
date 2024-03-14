# def solve(r1,c1,list,number):
#         for x
#         if list[r1][c1]=="L":
#                 number+=10
#         if list[r1][c1]=="m":
#                 number+=5
#         if list[r1][c1]=="s":
#                 number+=1





a=int(input())
b=int(input())
list=[]
for x in range(b):
   c=input()
   list.append(c)
d=int(input())
e=int(input())
number=0
# r1=0
# c1=0
# print(solve(r1,c1,d,e,list))
for x in list:
    for y in range(a):
        if x[y]=="L":
            number+=10
        if x[y]=="M":
            number+=5
        if x[y]=="S":
            number+=1
print(number)

