class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposite(self,amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f"Previous balance {amount} new amount {self.balance}")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self,amount):
        if amount > self.balance:
            print("You can not withdraw")
        else:
            self.balance = self.balance - amount
            print(f"Withdrew {amount}. New balance is {self.balance}")
        

account = BankAccount("khadija",1000)


account.withdraw(20011)
