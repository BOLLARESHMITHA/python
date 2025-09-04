def perfect_num(num):
    sum_n=0
    o_n=num
    for i in range(1,num):
        if(num%i==0):
            sum_n+=i
    if(num==sum_n):
        print(num," is perfect number")
    else:
        print(num," is not perfect number")        
n=int(input("enter number = "))
perfect_num(n)