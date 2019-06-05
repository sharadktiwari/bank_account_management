print("......BANK.....")

class bank:
    def __init__(self):
        self.bankd={}

    def openacc(self):
        self.name=input("enter account holder name = ")
        self.accno=int(input("enter account number = "))
        self.balance=int(input("enter balance = "))
        self.bankd[self.name]=[self.accno,self.balance]
    def showallacc(self):
        if len(self.bankd.keys())==0:
            print("No account opened.....")
        else:
            for k,v in self.bankd.items():
                print(f"name = {k}, account no. = {v[0]}, balance = {v[1]}")
    def showacc(self):
        accname=input("enter account holder name whose account detail you want to see = ")
        d=self.bankd[accname]
        if d:
            print(f"name = {accname}, account no. = {d[0]}, balance = {d[1]}")
        else:
            print("No record found.....")
    def diposit(self):
        accname=input("enter account holder name whom account's you want to deposit rupees = ")
        amt=int(input("enter amount you want to deposit = "))
        d=self.bankd[accname]
        d[1]+=amt
        print(f"{amt} rupees deposited to acc no. - {d[0]}")

    def withdraw(self):
        accname=input("enter account holder name whom account's you want to withdraw rupees = ")
        d=self.bankd[accname]
        amt=int(input("enter amount you want to withdraw = "))
        if amt<=d[1]:
            d[1]-=amt
        else:
            print("not enough money")
        print(f"{amt} rupees withdrawed from acc no. - {d[0]}")

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

