def num_alpha_digi_special(s):
    a=d=sp=0
    for i in range(0,len(s)):
        if(s[i].isalpha()):
            a+=1
        elif(s[i].isdigit()):
            d+=1
        else:
            sp+=1
    print("In string ",s,"\nNo of alphabet = ",a,"\nNo of digits = ",d,"\nNo of special characters = ",sp)

s=input("enter the string : ")
num_alpha_digi_special(s)