def prime_n(num):
    c=2
    i=2
    while(i<num):
        if(num%i==0):
            c+=1
        i+=1
    if(c>2):
        print(num," is not a prime number")
    else:
        print(num," is prime number")
n=int(input("enter number = "))
prime_n(n)