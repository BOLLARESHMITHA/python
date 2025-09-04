def all_perfect(num):
    for i in range(1,num+1):
        sum_n=0
        for j in range(1,i):
            if(i%j==0):
                sum_n+=j
        if(i==sum_n):
            print(i,end=" ")
n=int(input("enter number = "))
print("Perfect numbers between 1 to ",n," are :")
all_perfect(n)