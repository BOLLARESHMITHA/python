def pat_s(num):
    for i in range(1,num+1):
        for j in range(1,num+1):
            if(i==j):
                print("$",end=" ")
            else:
                print("*",end=" ")
        print()
n=int(input("enter number = "))
pat_s(n)