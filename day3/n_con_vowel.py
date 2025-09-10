def num_consonent_vowel(s):
    c=v=0
    for i in range(0,len(s)):
        if(s[i].isalpha()):
            if(s[i] in ['a','e','o','i','u']):
                v+=1
            else:
                c+=1
    print("In string ",s,"\nNo of consonents = ",c,"\nNo of vowels = ",v)

s=input("enter the string : ")
num_consonent_vowel(s)