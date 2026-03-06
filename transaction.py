from account import Account, AccountManager

class Transaction:
    def __init__(self, account: Account):
        self.account = account

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.account.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.account.balance:
            raise ValueError("Insufficient funds.")
        self.account.balance -= amount