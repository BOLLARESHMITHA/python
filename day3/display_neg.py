def ele_neg(l):
    r=list()
    for i in l:
        if(i<0):
            r.append(i)
    return r
l=[]
n=int(input("enter the number of element to insert : "))
for i in range(n):
    ele=int(input("enter the element : "))
    l.append(ele)
if(len(ele_neg(l))!=0):
    print(ele_neg(l))
else:
    print("no negative items")