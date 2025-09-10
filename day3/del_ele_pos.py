def delete_ele(l,pos):
    r=[]
    for i in range(1,len(l)+1):
        if(i!=pos):
            r.append(l[i-1])
    return r
l=[]
n=int(input("enter the number of element to insert : "))
for i in range(n):
    ele=int(input("enter the element : "))
    l.append(ele)
if(len(l)!=0):
    pos_ele=int(input("enter pos of element to delete : "))
    print("list =",delete_ele(l,pos_ele))
else:
    print("no items")