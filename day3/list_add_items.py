def inset_ele(l,ele):
    l=l+[ele]
    return l


l=[]
n=int(input("enter the number of element to insert : "))
for i in range(n):
    ele=int(input("enter the element : "))
    l=inset_ele(l,ele)
print(l)
