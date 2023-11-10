from abc import ABC, abstractmethod
from src.domain.transaction_entity import TransactionEntity
from typing import List

class TransactionRepositoryAbstract(ABC):
    @abstractmethod
    def save_transaction(self, transaction: TransactionEntity) -> None:
        """Save transaction"""

    @abstractmethod
    def get_transactions(self, account_id: int) -> List[TransactionEntity]:
        """Save transaction"""