#Crossword Puzzele


# In this program , you will have two inputs. the programe will determine if the first input include the second input. 
# for example: first input: cedsghkadsfgh    second input ced     print yes   
# if first input ader     second input qwe print no




def put1():
    item1=input(" what do you want put in the line ")
    return (item1)
def put2():  
    item2=input(" what things do you want to find from the line ")
    return (item2)
def loop_1(input1,input2,search,sign):

    lenth=len(input2)
    for x in input1:      
        len_search=len(search)
        if len_search<lenth:
            search+=x
        else: 
            if search==input2:
                sign=False
                print("yes, you can find want you put in the line")
                break
            else:
                search=search[1:]
                search+=x
    if sign==True:
        print("sorry, the line isn't include your input")
input1=put1()
input2=put2()
search=""
sign=True
loop_1(input1,input2,search,sign)
