
import hashlib

class BankAccount:
    def __init__(self, username, password):  
        self.username = username
        self.password = self.hash_password(password)
        self.balance = 0
        self.transaction_history = []

    def hash_password(self, password):
        
        return hashlib.sha256(password.encode()).hexdigest()

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount}")
            return True
        return False

    def withdraw(self, amount):
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            return True
        return False

    def transfer(self, amount, recipient_account):
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            recipient_account.balance += amount
            self.transaction_history.append(f"Transferred: ${amount} to {recipient_account.username}")
            return True
        return False

    def check_balance(self):
        return self.balance

    def view_history(self):
        return self.transaction_history


class BankingSystem:
    def __init__(self): 
        self.accounts = {}

    def create_account(self, username, password):
        if username not in self.accounts:
            self.accounts[username] = BankAccount(username, password)
            return f"Account created for {username}"
        return "Username already taken."

    def login(self, username, password):
        if username in self.accounts and self.accounts[username].password == hashlib.sha256(password.encode()).hexdigest():
            return self.accounts[username]
        return None

# Example usage
bank = BankingSystem()
print(bank.create_account('user1', 'password123'))
user = bank.login('user1', 'password123')

if user:
    print("Login successful!")
    user.deposit(100) 
    print(f"Balance: ${user.check_balance()}")
    user.withdraw(50)  
    print(f"Balance: ${user.check_balance()}")
    print(user.view_history()) 
else:
    print("Invalid login credentials.")
