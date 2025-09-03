def add():
    print("function with out any parameter and no return statement")
    a=10
    b=20
    print("a = ",a," ,b = ",b)
    s=a+b
    print("a+b =",s)
def sub(a,b):
    print("function with parameters and no return statement")
    print("a = ",a," ,b = ",b)
    s=a-b
    print("a-b =",s)
def mul(a,b):
    print("function with parameters and return statement")
    print("a = ",a," ,b = ",b)
    s=a*b
    return s
def div():
    print("function with no parameters and return statement")
    a=10
    b=10
    s=a/b
    return s
add()
sub(10,20)
res_m=mul(10,20)
print("a * b = ",res_m)
res_d=div()
print("a / b = ",res_d)
