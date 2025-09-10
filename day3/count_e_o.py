def odd_even(l):
    e=o=0
    for i in l:
        if(i%2==0):
            e+=1
        else:
            o+=1
    return o,e
l=[]
n=int(input("enter the number of element to insert : "))
for i in range(n):
    ele=int(input("enter the element : "))
    l.append(ele)
if(len(l)!=0):
    odd,even=odd_even(l)
    print("odd element count = ",odd," even element count = ",even)
else:
    print("no items")