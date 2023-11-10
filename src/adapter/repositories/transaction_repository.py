from src.domain.transaction_entity import TransactionEntity
from typing import List


class TransactionRepository:
    def __init__(self):
        self.transactions = {}

    def save_transaction(self, transaction: TransactionEntity) -> None:
        if not self.transactions.get(transaction.account_id):
            self.transactions[transaction.account_id] = [transaction]
        else:
            self.transactions[transaction.account_id].append(transaction)

    def get_transactions(self, account_id: int) -> TransactionEntity:
        return self.transactions.get(account_id, [])
