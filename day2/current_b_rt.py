def cal_current_bill(nu,na,t):
    rem=t
    cost=0
    if(rem>50):
        cost+=(50*3.8)
        rem-=50
        if(rem>50):
            cost+=(50*4.2)
            rem-=50
            if(rem>100):
                cost+=(100*5.10)
                rem-=100
                if(rem>100):
                    cost+=(100*6.30)
                    rem-=100
                    if(rem>0):
                        cost+=(rem*7.50)
                else:
                    cost+=(rem*6.30)
            else:
                cost+=(rem*5.10)
        else:
            cost+=(rem*4.2)
    else:
        cost+=(rem*3.8)
    print(cost)


con_number=int(input("enter consumer number ="))
con_name=input("enter consumer name = ")
pmr,lmr=map(float,input("present and last month reading = ").split(" "))
#lmr=float(input("last month reading = "))
total_units=pmr-lmr
cal_current_bill(con_number,con_name,total_units)