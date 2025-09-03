cost_per_unit=3.80

con_number=int(input("enter consumer number ="))
con_name=input("enter consumer name = ")
pmr=float(input("present month reading = "))
lmr=float(input("last month reading = "))

total_units=pmr-lmr
c_bill=total_units*cost_per_unit

print("current bill")
print("consumer number :",con_number,"\nname :",con_name)
print("total number of units =",total_units)
print("current bill = ",round(c_bill,0))

msg=f"hello {con_name} thank u for paying bill of amt {round(c_bill)}"
print(msg)
