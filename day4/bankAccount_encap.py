class BankAccount:
    def __init__(self):
        self.__balance=0
    def deposit(self,amt):
        self.__balance+=amt

    def withdraw(self,amt):
        if(self.__balance>=amt):
            self.__balance-=amt
        else:
            print("insufficient balance")
    def get_balance(self):
        return self.__balance

    
ba=BankAccount()
d=int(input("deposit "))
w=int(input("withdraw "))
ba.deposit(d)
ba.withdraw(w)
print(ba.get_balance())