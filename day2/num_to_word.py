def n_to_w(num):
    d=""
    if(num%2==0):
        if(num==0):
            d="zero"
        elif(num==2):
            d="Two"
        elif(num==4):
            d="four"
        elif(num==6):
            d="six"
        else:
            d="Eight"
    else:
        if(num==1):
            d="One"
        elif(num==3):
            d="Three"
        elif(num==5):
            d="Five"
        elif(num==7):
            d="Seven"
        else:
            d="Nine"
    return d
def div(num):
    rem=0
    s=""
    while(num>0):
        rem=num%10
        s=n_to_w(rem)+s
        s=" "+s
        num//=10
    print(s)
n=int(input("enter number = "))
div(n)