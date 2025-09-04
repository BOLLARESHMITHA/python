def armstrong_n(num):
    sum_n=0
    o_n=num
    while(num>0):
        sum_n+=(num%10)**3
        num//=10
    if(o_n==sum_n):
        print(o_n," is armstrong number ")
    else:
        print(o_n,"is not armstrong number")
n=int(input("enter number = "))
armstrong_n(n)