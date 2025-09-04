def getSumOf_L_1(num):
    o_n=num
    sum_n=num%10
    l=num%10
    while(num>9):
        num//=10
    f=num
    sum_n+=f
    print(o_n ,"=> last number = ",l,", first number = ",f)
    print("sum of last and first number = ",sum_n)
n=input("enter number = ")
print("count of number in ",n," = ",len(n))
getSumOf_L_1(int(n))