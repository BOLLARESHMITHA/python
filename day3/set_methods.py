s=set()

n=int(input("No of elements to insert in set = "))
for i in range(n):
    ele_a=input("enter element to add = ")
    s.add(ele_a)

ele_r=(input("enter element to remove = "))
print("removing element using remove()")
print(s.remove(ele_r)," set after remove method ",s)

print("removing using pop()")
print(s.pop()," set after pop method ",s)

print("remoing all elements using clear()")
print(s.clear," set after clear method ",s)



