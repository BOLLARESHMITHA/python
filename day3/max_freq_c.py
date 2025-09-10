def freq_char(s):
    v=[]
    a=""
    max_f=0
    for i in range(0,len(s)):
        if(s[i] not in v):
            f=1
            for j in range(i+1,len(s)):
                if(s[i]==s[j]):
                    f+=1
            v.append(s[i])
            if(max_f<f):
                max_f=f
                a=s[i]
    print("character ",a," is most repeated char in ",s," and no times repeated = ",max_f)

s=input("enter the string : ")
freq_char(s)