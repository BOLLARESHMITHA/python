def sum_of_nums(num):
    sum_n=0
    while(num>0):
        sum_n+=num%10
        num//=10
    print(sum_n)
n=int(input("enter number = "))
sum_of_nums(n)