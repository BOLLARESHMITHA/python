#convert kilometers to miles
def convert(kms):
    m=kms*0.62137119
    return m
n=int(input("enter no of kms ="))
m=convert(n)
print(round(m,5))