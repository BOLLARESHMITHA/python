def all_factors(num):
    for i in range(1,num):
        if(num%i==0):
            print(i,end=" ")
n=int(input("enter number = "))
print("All factors of ",n)
all_factors(n)