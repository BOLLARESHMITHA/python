p=int(input("enter principle amount = "))
r=int(input("enter rate of interest "))
t=int(input("enter no of months ="))

si=(p*r*t)/100
total_amt=si+p

print("simple interest = ",si," total amt = ",total_amt)