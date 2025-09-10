def uni_ele(l):
    visit=uni=[]
    for i in range(0,len(l)):
        f=1
        if(l[i] not in visit):
            for j in range(i+1,len(l)):
                if(i!=j and l[i]==l[j]):
                    f+=1
            visit.append(l[i])
            if(f==1):
                uni.append(l[i])
    return uni
l=[]
n=int(input("enter the number of element to insert : "))
for i in range(n):
    ele=int(input("enter the element : "))
    l.append(ele)
if(len(l)!=0):
    print("unique elements : ",uni_ele(l))
else:
    print("no items")