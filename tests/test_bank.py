import pytest
from bank import Bank


def test_create_customer():
    bank = Bank()
    customer = bank.create_customer("John Doe")
    assert customer.name == "John Doe"


def test_create_account():
    bank = Bank()
    customer = bank.create_customer("John Doe")
    account = bank.create_account(customer.customer_id, 100.0)
    assert account is not None


def test_perform_transaction():
    bank = Bank()
    customer = bank.create_customer("John Doe")
    account = bank.create_account(customer.customer_id, 100.0)
    transaction = bank.perform_transaction(account.account_id, 50)
    assert account.get_balance() == 50.0


def test_get_customer_accounts():
    bank = Bank()
    customer = bank.create_customer("John Doe")
    bank.create_account(customer.customer_id, 100.0)
    accounts = bank.get_customer_accounts(customer.customer_id)
    assert len(accounts) == 1