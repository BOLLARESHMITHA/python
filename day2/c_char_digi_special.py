#take any character as I/P and gives wherther char(lower,upper),digit,special
def check_c_d_s(c):
    if(c.isalpha()):
        if(c.isupper()):
            print("is upper character")
        else:
            print("is lower character")
    elif(c.isdigit()):
        print("is digit")
    else:
        print("is special")
a=input("enter on letter = ")
check_c_d_s(a)