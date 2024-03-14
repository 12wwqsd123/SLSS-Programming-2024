#David Wang
#March 7th
# a program to detemine if the number is a prime number and its fators
def main(a,list1,ind):
    for x in range(1,a+1):
        if a%x==0:
            ind+=1
            list1.append(x)
    return list1,ind
a=int(input(" choose a number that you like "))
list1=[]
ind=0
first=main(a,list1,ind)[0]
second=main(a,list1,ind)[1]
if second<=2:
    print(f"the factor of this number is{first}. moreover, this number is a prime number")

else:
     print(f"the factor of this number is{first}. moreover, this number is not a prime number")




            

