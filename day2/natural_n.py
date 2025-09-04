def natural_num(num):
    while(num>0):
        print(num,end="  ")
        num-=1
n=int(input("enter number of natural number to print = "))
natural_num(n)