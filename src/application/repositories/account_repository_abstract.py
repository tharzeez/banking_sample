from abc import ABC, abstractmethod
import typing

from src.domain.account_entity import AccountEntity


class AccountRepositoryAbstract(ABC):
    @abstractmethod
    def save_account(self, account: AccountEntity) -> None:
        """Save account"""

    @abstractmethod
    def find_account_by_id(self, account_id) -> AccountEntity:
        """Find the account details by account id"""

    @abstractmethod
    def find_accounts_by_customer_id(self, customer_id) -> typing.List[AccountEntity]:
        """Find all the accounts of a customer by customer id"""

    @abstractmethod
    def get_accounts_count(self) -> int:
        """Find the account details by account id"""