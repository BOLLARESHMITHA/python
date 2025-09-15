def division(num,den):
    try:
        div=num/den
        print("division of ",num," & ",den," is =",div)
    except ZeroDivisionError:
        print("denominator(den) should be > zero")
    else:
        print("division completed successfully")
    finally:
        print("Thank U")


num=int(input("enter numberator = "))
den=int(input("enter denominator = "))
division(num,den)