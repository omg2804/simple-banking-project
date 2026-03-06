# bank.py

from account import Account, AccountManager
from customer import Customer
from transaction import Transaction

class Bank:
    def __init__(self):
        self.account_manager = AccountManager()
        self.customers = {}

    def create_customer(self, name, email):  # Added email parameter
        customer = Customer(name, email)  # Pass email to Customer
        self.customers[customer.id] = customer
        return customer

    def create_account(self, customer_id, initial_balance=0):
        if customer_id not in self.customers:
            raise ValueError("Customer not found.")
        account = self.account_manager.create_account(customer_id, initial_balance)
        return account

    def perform_transaction(self, account_id, amount):
        account = self.account_manager.get_account(account_id)
        transaction = Transaction(account, amount)
        transaction.process()
        return transaction

    def get_customer_accounts(self, customer_id):
        if customer_id not in self.customers:
            raise ValueError("Customer not found.")
        return self.account_manager.get_accounts_by_customer(customer_id)