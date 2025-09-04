def fact(num):
    f=1
    for i in range(1,num):
        print(i,end='*')
        f*=i
    print(num,end="=")
    f*=num
    print(f)
n=int(input("enter number"))
print(" factorial of ",n,"! = ",end="  ")
fact(n)
