class BankAccount:
    def __init__(self, fullName, accountNumber, routingNumber, balance):
        self.fullName=fullName
        self.accountNumber=accountNumber
        self.routingNumber=routingNumber
        self.balance=balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Amount Deposited: {amount}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds. Overdraft charged. ($10)")
            self.balance -= 10
        else:
            self.balance -= amount
            print(f"Amount Withdrawn {amount}")
    def getBalance(self):
        print(f"Account balance: {self.balance}")
        return self.balance
    def addInterest(self):
        self.balance += (self.balance*0.00083)
    def printReciept(self):
        print(self.fullName)
        print(f"Account No.: {self.accountNumber}")
        print(f"Routing No.: {self.routingNumber}")
        print(f"Balance: {self.balance}")

#Testing~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Account1
account1=BankAccount("player1", 1, 1, 0)
account1.deposit(10)
account1.printReciept()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#Account2
account2=BankAccount("player2", 2, 2, 0)
account2.withdraw(500)
account2.getBalance()
account2.printReciept()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#Account3
account3=BankAccount("player3", 3, 3, 1000)
account3.addInterest()
account3.printReciept()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")