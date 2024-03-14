#Modules
#Author
#11 March 2024

import random
def coin_flip():
    result=random.random()

    if result<0.5:
        return"heads"
    elif result<0.999999:
        return"tails"
    else:
        return"others"
def draw_card():
    result1=random.randrange(1,14)
    if result1=="1":
        return "A"
    if result1=="1":
        return "A"
    if result1=="1":
        return "A"
def main():
    head=0
    tail=0
    other=0
    for _ in range(10000000):
        if coin_flip()=="others":
            other+=1
        if coin_flip()=="heads":
            head+=1
        if coin_flip()=="tails":
            tail+=1
        
    print(f"other:{other}")
    print(f"head:{head}")
    print(f"tail:({tail}")
main()