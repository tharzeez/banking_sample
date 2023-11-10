from src.domain.base_entity import BaseEntity


class TransactionEntity(BaseEntity):
    def __init__(self, customer_id: int, account_id: int, amount: int, txn_type: str) -> None:
        super().__init__()
        self.customer_id = customer_id
        self.account_id = account_id
        self.amount = amount
        self.txn_type = txn_type
