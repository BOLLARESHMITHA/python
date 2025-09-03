def min_3():
    a, b, c = map(int, input("enter values : ").split())
    if(a<b and a<c):
        return a
    elif(b<a and b<c):
        return b
    else:
        return c
res=min_3()
print("minimum value of given values : ",res)