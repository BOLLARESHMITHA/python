'''
std is pass or fail

if pass --> grade
    <50  -> c
    51-70 ->b
    71-80 -> a
    >80 ->distension
<40 -> fail
'''

def std_reportc(no,na,m1,m2,m3):
    
    print("student report")
    print("roll no :",std_number,"\nname :",std_name,"\nmarks")
    print("math :",math," phy :",phy," eng :",eng)

    avg_marks=(math+phy+eng)/3
    g=""
    if(avg_marks>=40):
        if(avg_marks<=50):
            g="C"
        elif(avg_marks>=51 and avg_marks<=70):
            g="B"
        elif(avg_marks>=71 and avg_marks<=80):
            g="A"
        else:
            g="distension"
    else:
        g="fail"

    print("avg of marks = ",round(avg_marks,2))
    print("grade = ",g)

std_number=input("enter std roll no =")
std_name=input("enter std name = ")

math=int(input("enter marks for math ="))
phy=int(input("enter marks for phy ="))
eng=int(input("enter marks for eng ="))
std_reportc(std_number,std_name,math,phy,eng)