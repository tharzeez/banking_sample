from typing import Optional, List
from src.domain.account_entity import AccountEntity


class AccountRepository:
    def __init__(self):
        self.accounts = []

    def save_account(self, account: AccountEntity) -> None:
        self.accounts.append(account)

    def find_account_by_id(self, account_id: int) -> Optional[AccountEntity]:
        for account in self.accounts:
            if account.account_id == account_id:
                return account
        return None

    def find_accounts_by_customer_id(self, customer_id) -> List[AccountEntity]:
        return [account for account in self.accounts if account.customer_id == customer_id]

    def get_accounts_count(self) -> int:
        return len(self.accounts)
