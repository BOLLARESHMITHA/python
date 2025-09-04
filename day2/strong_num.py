def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)

def strong_n(num):
    sum_f=0
    o_n=num
    while(num>0):
        sum_f+=fact(num%10)
        num//=10
    if(o_n==sum_f):
        print(o_n ," is strong number")
    else:
        print(o_n," is not strong number")
n=int(input("enter number = "))
strong_n(n)
    