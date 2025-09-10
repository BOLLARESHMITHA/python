def freq_ele(l):
    v=[]
    for i in range(0,len(l)):
        f=1
        if(l[i] not in v):
            for j in range(i+1,len(l)):
                if(i!=j and l[i]==l[j]):
                    f+=1
            print("freq of element ",l[i]," = ",f)
            v.append(l[i])
l=[]
n=int(input("enter the number of element to insert : "))
for i in range(n):
    ele=int(input("enter the element : "))
    l.append(ele)
if(len(l)!=0):
    freq_ele(l)
else:
    print("no items")