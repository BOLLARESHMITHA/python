def char_occurrences(s,c):
    O=[]
    for i in range(0,len(s)):
        if(s[i]==c):
            print(i+1,"th, ",sep="",end="")


s=input("enter the string : ")
c=input("enter the character : ")
print("In string ",s," character ",c," found in positions is = ",end="")
char_occurrences(s,c)