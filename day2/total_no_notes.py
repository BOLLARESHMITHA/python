def no_of_notes(amt):
    rem=amt
    c=0
    while(rem>0):
        if(rem>=2000):
            c+=rem//2000
            rem-=2000*(rem//2000)
        elif(rem>=500 and rem<2000):
            c+=rem//500
            rem-=500*(rem//500)
        elif(rem>=200 and rem<500):
            c+=rem//200
            rem-=200*(rem//200)
        elif(rem>=100 and rem<200):
            c+=rem//100
            rem-=100*(rem//100)
        elif(rem>=50 and rem<100):
            c+=rem//50
            rem-=50*(rem//50)
        elif(rem>=20 and rem<50):
            c+=rem//20
            rem-=20*(rem//20)
        elif(rem>=10 and rem<20):
            c+=rem//10
            rem-=10*(rem//10)
        elif(rem>=5 and rem<10):
            c+=rem//5
            rem-=5*(rem//5)
        elif(rem>=2 and rem<5):
            c+=rem//2
            rem-=2*(rem//2)
        else:
            c+=1
            rem-=1
    print(c)

n=int(input("enter amt = "))
no_of_notes(n)