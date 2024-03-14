# February 29th
#David Wang
def main():
    a=input()
    a=a.split(" ")
    stay=""
    return translation(a,stay)
def translation(a,stay):
    for x in a:
        if x=="100":
            x="💯"
        if x=="noodle":
            x="🍜"
        stay+= x
        stay+=" "
    return stay
print(main())

