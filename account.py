class Account:
    def __init__(self, account_id, account_holder, balance=0.0):
        self.account_id = account_id
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account ID: {self.account_id}, Holder: {self.account_holder}, Balance: {self.balance:.2f}"

class AccountManager:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_id, account_holder):
        if account_id not in self.accounts:
            self.accounts[account_id] = Account(account_id, account_holder)
            return True
        return False

    def delete_account(self, account_id):
        if account_id in self.accounts:
            del self.accounts[account_id]
            return True
        return False

    def get_account(self, account_id):
        return self.accounts.get(account_id, None)

    def list_accounts(self):
        return [str(account) for account in self.accounts.values()]