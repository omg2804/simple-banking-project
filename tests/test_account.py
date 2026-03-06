import pytest
from account import Account, AccountManager


def test_account_initialization():
    account = Account("12345", "John Doe", 100.0)
    assert account.account_id == "12345"
    assert account.account_holder == "John Doe"
    assert account.get_balance() == 100.0


def test_account_deposit():
    account = Account("12345", "John Doe")
    assert account.deposit(50) is True
    assert account.get_balance() == 50.0
    assert account.deposit(-10) is False


def test_account_withdraw():
    account = Account("12345", "John Doe", 100.0)
    assert account.withdraw(50) is True
    assert account.get_balance() == 50.0
    assert account.withdraw(100) is False


def test_account_str():
    account = Account("12345", "John Doe", 100.0)
    assert str(account) == "Account ID: 12345, Holder: John Doe, Balance: 100.00"


def test_account_manager():
    manager = AccountManager()
    assert manager.create_account("12345", "John Doe") is True
    assert manager.create_account("12345", "Jane Doe") is False
    assert manager.get_account("12345") is not None
    assert manager.delete_account("12345") is True
    assert manager.get_account("12345") is None