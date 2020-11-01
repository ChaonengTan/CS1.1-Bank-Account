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
        if amount >= self.balance:
            self.balance -= amount
            print(f"Amount Withdrawn {amount}")
        else:
            print("Insufficient Funds. Overdraft charged. ($10)")
            self.balance -= 10
    def getBalance(self):
        print(f"Account balance: {self.balance}")
        return self.balance
    def addInterest(self):
        self.balance *= 0.00083
    def printReciept(self):
        print(self.fullName)
        print(f"Account No.: {self.accountNumber}")
        print(f"Routing No.: {self.routingNumber}")
        print(f"Balance: {self.balance}")
#Testing
newAccount=BankAccount("Chao", 1, 1, 0)
newAccount.deposit(10)
print(newAccount.__dict__)
newAccount.printReciept()