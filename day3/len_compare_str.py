def find_len(s):
    len_str=0
    for i in s:
        len_str+=1
    return len_str

def compare_s(s1,s2):
    if(s1==s2):
        print("strings ",s1," and ",s2," are same ")
    else:
        print("strings ",s1," and ",s2," are different ")

def concat_s(s1,s2):
    new_s=s1+s2
    print("concatenate of ",s1," and ",s2," is = ",new_s)


while(True):

    ch=int(input("Enter choice :"))

    if(ch>=1 and ch<=3):
        if(ch==1):
            s=input("enter string = ")
            print("length of string ",s," is = ",find_len(s))
        elif(ch==2):
            s1=input("enter string = ")
            s2=input("enter string = ")
            compare_s(s1,s2)
        elif(ch==3):
            s1=input("enter string = ")
            s2=input("enter string = ")
            concat_s(s1,s2)
    else:
        break
