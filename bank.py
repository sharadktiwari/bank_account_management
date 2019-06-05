print("......BANK.....")

class bank:
    def __init__(self):
        self.bankd={}

    def openacc(self):
        self.name=input("enter account holder name = ")
        self.accno=int(input("enter account number = "))
        self.balance=int(input("enter balance = "))
        self.bankd[self.accno]=[self.name,self.balance]
    def showallacc(self):
        if len(self.bankd.keys())==0:
            print("No account opened.....")
        else:
            for k,v in self.bankd.items():
                print(f"account no. = {k}, name = {v[0]}, balance = {v[1]}")
    def showacc(self):
        accno=int(input("enter account number whose account detail you want to see = "))
        d=self.bankd[accno]
        if d:
            print(f"account no. = {accno}, name = {d[0]},  balance = {d[1]}")
        else:
            print("No record found.....")
    def diposit(self):
        accno=int(input("enter account number whom account's you want to deposit rupees = "))
        amt=int(input("enter amount you want to deposit = "))
        d=self.bankd[accno]
        d[1]+=amt
        print(f"{amt} rupees deposited to acc no. - {accno}")

    def withdraw(self):
        accno=int(input("enter account number whom account's you want to withdraw rupees = "))
        d=self.bankd[accno]
        amt=int(input("enter amount you want to withdraw = "))
        if amt<=d[1]:
            d[1]-=amt
        else:
            print("not enough money")
        print(f"{amt} rupees withdrawed from acc no. - {accno}")

print(".....main menu.....")
print("1. open account")
print("2. show all accounts")
print("3. show account through name")
print("4. deposit")
print("5. withdraw")
print("6. exit")

B=bank()
while True:
    choice=int(input("enter your choice = "))
    if choice==1:
        B.openacc()
    elif choice==2:
        B.showallacc()
    elif choice==3:
        B.showacc()
    elif choice==4:
        B.diposit()
    elif choice==5:
        B.withdraw()
    elif choice==6:
        break
    else:
        print("enter valid number..")

