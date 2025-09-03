def c_leapYear(num):
    if(num%4==0):
        if(num%100==0):
            if(num%400==0):
                print("leap year")
            else:
                print("not leap year")
        else:
            print("not leap year")
    else:
        print("not leap year")
n=int(input("enter number = "))
c_leapYear(n)