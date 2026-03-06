import pytest
from account import Account
from transaction import Transaction


def test_transaction_deposit():
    account = Account("12345", "John Doe")
    transaction = Transaction(account)
    transaction.deposit(100)
    assert account.get_balance() == 100.0
    with pytest.raises(ValueError):
        transaction.deposit(-50)


def test_transaction_withdraw():
    account = Account("12345", "John Doe", 100.0)
    transaction = Transaction(account)
    transaction.withdraw(50)
    assert account.get_balance() == 50.0
    with pytest.raises(ValueError):
        transaction.withdraw(100)
    with pytest.raises(ValueError):
        transaction.withdraw(-10)