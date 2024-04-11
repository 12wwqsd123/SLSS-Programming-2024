#Loops and Iteration
#Author 
# 5 April 2024
for _ in range(10):
    print("something)")
grocery_list=["bluueberry mufflins",'potato chips',"aluminium foil","orange juice","RTX 4070 Super","cereal"]
for x in grocery_list:
    if x.lower =="rtx 4070 super":
        break
    print(f"*{x}")
for x in range(100):
    if(x+1)%2==0:
        print(f"{x+1} is even")
    else:
        print(f"{x+1} is odd")
def pyramid (base_width:int):
    