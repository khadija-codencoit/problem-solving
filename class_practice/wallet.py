# Wallet App

# Create a Wallet class with:
# Attributes: owner, balance
# Methods: add_money(amount), spend_money(amount), show_balance()

class Wallet:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def add_money(self,amount):
        if amount > 0:
            amount = amount + self.balance
            print(f"Previous Balance {amount} New Blance {amount}")
        else:
            print("Negative balance is not allowed")  

    def withdraw(self,amount):
        if amount > self.balance:
            print("You can not withdraw")
        else:
            self.balance = self.balance - amount
            print(f"Your current balance is {self.balance}")

    def show_balance(self):
        print(f"{self.owner} and new balance {self.balance}")

wallet = Wallet("Naimul Alom",20000)
wallet.show_balance()
wallet.withdraw(5000)
wallet.add_money(80000)











            
               

my_wallet = Wallet("Khadija", 500)
print(my_wallet)
