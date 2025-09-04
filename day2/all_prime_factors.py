def prime_n(num):
    c=2
    i=2
    while(i<num):
        if(num%i==0):
            c+=1
        i+=1
    if(c>2):
        return False
    else:
        return True 
def all_factors(num):
    for i in range(1,num):
        if(num%i==0):
            if(prime_n(i)):
            print(i,end=" ")
n=int(input("enter number = "))
print("All factors of ",n)
all_factors(n)