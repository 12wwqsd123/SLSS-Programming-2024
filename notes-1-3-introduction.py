#Methods(Strings)
#name: David
#22 February 2024
# weather = input("what is the weather like")
# if weather.lower().strip("!.?,")== "rainy":
#     print(" you'll need an umbrella")
# else:
#     print(f"sprry, I don't understand{weather}.")
a=input("whould you like fries with your meal?")

if a.lower()=="yes":
    print("yes, this is the meal with fries")
if a.lower().title()=="no":
    print(" this is the meal without fries")
if a.lower()!="yes"and a.lower()!="no":
    print(f"Sorry, I don't understand {a}")
