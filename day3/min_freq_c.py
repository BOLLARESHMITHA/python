def freq_char(s):
    v=[]
    a=""
    min_f=len(s)
    for i in range(0,len(s)):
        if(s[i] not in v):
            f=1
            for j in range(i+1,len(s)):
                if(s[i]==s[j]):
                    f+=1
            v.append(s[i])
            if(min_f>f):
                min_f=f
                a=s[i]
    print("character ",a," is least repeated char in ",s," and no times repeated = ",min_f)

s=input("enter the string : ")
freq_char(s)