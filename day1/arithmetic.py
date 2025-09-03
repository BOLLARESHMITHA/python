def add(a,b):
    print("a = ",a," ,b = ",b)
    s=a+b
    return s
def sub(a,b):
    print("a = ",a," ,b = ",b)
    s=a-b
    return s
def mul(a,b):
    print("a = ",a," ,b = ",b)
    s=a*b
    return s
def div(a,b):
    if(b!=0):
        s=a/b
        return s
def floordiv(a,b):
    if(b!=0):
        s=a//b
        return s
def expo(a,b):
    s=a**b
    return s
op1=int(input("enter value = "))
op2=int(input("enter value = "))
print("sum of a,b = ",add(op1,op2))
print("sub of a,b = ",sub(op1,op2))
print("mul of a,b = ",mul(op1,op2))
print("div of a,b = ",div(op1,op2))
print("floor division of a,b = ",floordiv(op1,op2))
print("exponent of a,b = ",expo(op1,op2))
