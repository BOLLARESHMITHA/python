#take number of day as I/P and dayname as O/P
def DayName(num):
    d=""
    if(num%2==0):
        if(num==2):
            d="monday"
        elif(num==4):
            d="wednesday"
        else:
            d="friday"
    else:
        if(num==1):
            d="sunday"
        elif(num==3):
            d="Tuesday"
        elif(num==5):
            d="Thursday"
        else:
            d="sat"
    print(d)
n=int(input("enter day number = "))
if(n>0 and n<=7):
    DayName(n)
else:
    print("enter valid daynumber")

    