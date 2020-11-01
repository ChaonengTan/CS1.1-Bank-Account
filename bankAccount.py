from random import *
#creates a random 8 digit account number
def newAccountNumber():
    return randrange(10000000, 99999999)
class BankAccount:
    #initializes BankAccount with following attributes
    def __init__(self, fullName, routingNumber, balance=0):
        self.fullName=fullName
        self.accountNumber=newAccountNumber()
        self.routingNumber=routingNumber
        self.balance=balance
    #function adds indicated amount to balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Amount Deposited: {amount}")
    #function subtracts indicated amount from balance only if balance holds that much or greater.
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds. Overdraft charged. ($10)")
            self.balance -= 10
        else:
            self.balance -= amount
            print(f"Amount Withdrawn {amount}")
    #prints balance, returns balance
    def getBalance(self):
        print(f"Account balance: {self.balance}")
        return self.balance
    #adds interest?
    def addInterest(self):
        self.balance += (self.balance*0.00083)
    #prints information similar to __dict__ but formatted
    def printReciept(self):
        print(self.fullName)
        print(f"Account No.: {self.accountNumber}")
        print(f"Routing No.: {self.routingNumber}")
        print(f"Balance: {self.balance}")

#Testing~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Account1
account1=BankAccount("player1", 1)
account1.deposit(10)
account1.printReciept()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#Account2
account2=BankAccount("player2", 2)
account2.withdraw(500)
account2.getBalance()
account2.printReciept()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#Account3
account3=BankAccount("player3", 3, 1000)
account3.addInterest()
account3.printReciept()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")