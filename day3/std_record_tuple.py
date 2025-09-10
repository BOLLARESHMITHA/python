def Store_data_std(std_data,new_std):
    std_data.append(new_std)

def Std_topper_name(std_data):
    max_marks=0
    for i in range(0,len(std_data)):
        if(max_marks<std_data[i][2]):
            max_marks=std_data[i][2]
    for i in range(0,len(std_data)):
        if(std_data[i][2]==max_marks):
            return std_data[i][0]

def marks_above75(std_data):
    for i in range(0,len(std_data)):
        if(std_data[i][2]>75):
            print(std_data[i][0],end="\t")

std_data=[]

while(True):

    ch=int(input("Enter choice :"))

    if(ch>=1 and ch<=3):
        if(ch==1):
            name=input("enter name = ")
            roll=input("enter roll no = ")
            marks=int(input("enter marks = "))
            new_std=(name,roll,marks)
            Store_data_std(std_data,new_std)
        elif(ch==2):
            print("topper is ",Std_topper_name(std_data))
        elif(ch==3):
            print("std with marks above >75 is ")
            marks_above75(std_data)
    else:
        break
