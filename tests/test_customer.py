import pytest
from customer import Customer


def test_customer_initialization():
    customer = Customer("1", "John Doe", "john@example.com")
    assert customer.customer_id == "1"
    assert customer.name == "John Doe"
    assert customer.email == "john@example.com"


def test_customer_update_email():
    customer = Customer("1", "John Doe", "john@example.com")
    customer.update_email("john.doe@example.com")
    assert customer.email == "john.doe@example.com"


def test_customer_str():
    customer = Customer("1", "John Doe", "john@example.com")
    assert str(customer) == "Customer(ID: 1, Name: John Doe, Email: john@example.com)"