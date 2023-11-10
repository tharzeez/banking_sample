from src.domain.base_entity import BaseEntity
from src.domain.app_exception import AppException


class AccountEntity(BaseEntity):
    def __init__(self, account_id: int, customer_id: int, account_number: int, balance=0) -> None:
        super().__init__()
        self.account_id = account_id
        self.customer_id = customer_id
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            message = f"Insufficient funds to make a transaction for account {self.account_id}"
            raise AppException(message)

    def get_balance(self):
        return self.balance
