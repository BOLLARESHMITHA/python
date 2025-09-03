std_number=input("enter std roll no =")
std_name=input("enter std name = ")

math=int(input("enter marks for math ="))
phy=int(input("enter marks for phy ="))
eng=int(input("enter marks for eng ="))

avg_marks=(math+phy+eng)/3

print("student report")
print("roll no :",std_number,"\nname :",std_name,"\nmarks")
print("math :",math," phy :",phy," eng :",eng)
print("avg of marks = ",round(avg_marks,2))