def count_occurrences(s,c):
    o=0
    for i in range(0,len(s)):
        if(s[i]==c):
            o+=1
    return o


s=input("enter the string : ")
c=input("enter the character : ")
print("In string ",s," character ",c," found ",count_occurrences(s,c)," times")