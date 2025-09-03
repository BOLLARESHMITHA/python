def c_divby_5_11(num):
    if(num%5==0):
        if(num%11==0):
            print(num," is divisible by both 5 & 11")
        else:
            print(num," is divisible by 5 but not 11")
    else:
        print(num," is not divisible by both 5 & 11")
n=int(input("enter a number = "))
c_divby_5_11(n)