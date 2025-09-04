def palindrome_n(num):
    s=""
    o_n=num
    while(num>0):
        s+=str(num%10)
        num//=10
    if(o_n==int(s)):
        print(o_n," is palindrome number")
    else:
        print(o_n," is not palindrome number")
n=int(input("enter number = "))
if(len(str(n))>1):
    palindrome_n(n)
else:
    print(n," is palindrome number")