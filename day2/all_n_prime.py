def prime_n(num):
    for i in range(1,num+1):
        c=0
        for j in range(1,i+1):
            if(i%j==0):
                c+=1
        if(c==2):
            print(i,end="  ")
n=int(input("enter number = "))
print("prime number from 1 to ",n," is ")
prime_n(n)