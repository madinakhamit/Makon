class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds! Withdrawal not allowed.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

owner = input("Enter account owner's name: ")
balance = float(input("Enter initial balance: "))
account = Account(owner, balance)

while True:
    action = input("Enter 'deposit', 'withdraw', or 'exit': ").lower()
    
    if action == "deposit":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)
    
    elif action == "withdraw":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif action == "exit":
        print("Exiting banking system.")
        break

    else:
        print("Invalid option, try again.")
