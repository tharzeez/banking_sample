from src.utils.error_handling_utils import ErrorHandlingUtils
from src.domain.transaction_entity import TransactionEntity
from src.domain.app_exception import AppException
from src.application.repositories.transaction_repository_abstract import TransactionRepositoryAbstract
from typing import List


class AccountStatementUseCase:
    def __init__(self,
                 transaction_repository: TransactionRepositoryAbstract,
                 ) -> None:
        self.transaction_repository = transaction_repository

    def generate_account_statement(self, account_id: int) -> List[TransactionEntity]:
        try:
            all_transactions = self.transaction_repository.get_transactions(account_id)
            if all_transactions is None:
                raise AppException("Account doesn't exist")
            return all_transactions
        except Exception as exception:
            raise ErrorHandlingUtils.application_error("Account statement generation failed", exception)
