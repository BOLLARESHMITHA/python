def second_max_ele(l):
    first_max=max(l)
    second_max=-1000
    for i in l:
        if(i<first_max and i>second_max):
            second_max=i
    print(second_max)
l=[]
n=int(input("enter the number of element to insert : "))
for i in range(n):
    ele=int(input("enter the element : "))
    l.append(ele)
second_max_ele(l)