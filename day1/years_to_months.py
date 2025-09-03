def convert(d):
    y=d/365
    m=y*12
    print(d," days = ",y," in years and ",round(m,0)," in months")
days=int(input("enter number of days = "))
convert(days)