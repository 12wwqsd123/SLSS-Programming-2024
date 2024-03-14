#David Wang
#february 22
a=input("whould you like fries with your meal?")

if a.lower()=="yes":
    print("yes, this is the meal with fries")
if a.lower().title()=="no":
    print(" this is the meal without fries")
if a.lower()!="yes"and a.lower()!="no":
    print(f"Sorry, I don't understand {a}")
