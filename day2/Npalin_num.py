def palindrome_n(num):
    s=""
    o_n=num
    for i in range(1,num+1):
        s=""
        num=i
        while(num>0):
            s+=str(num%10)
            num//=10
        if(i==int(s)):
            print(i,end=" ")
n=int(input("enter number = "))
palindrome_n(n)