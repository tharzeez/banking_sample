from src.utils.error_handling_utils import ErrorHandlingUtils
from src.domain.transaction_entity import TransactionEntity
from src.domain.app_exception import AppException
from src.application.repositories.account_repository_abstract import AccountRepositoryAbstract
from src.application.repositories.transaction_repository_abstract import TransactionRepositoryAbstract


class TransactionUseCase:
    def __init__(self,
                 account_repository: AccountRepositoryAbstract,
                 transaction_repository: TransactionRepositoryAbstract
                 ) -> None:
        self.account_repository = account_repository
        self.transaction_repository = transaction_repository

    def make_transaction(self, account_id: int, amount: int, transaction_type: str) -> None:
        try:
            account_details = self.account_repository.find_account_by_id(account_id)
            if account_details is None:
                raise AppException("Account details not found")
            if transaction_type == 'deposit':
                account_details.deposit(amount)
            elif transaction_type == 'withdraw':
                account_details.withdraw(amount)
            else:
                raise AppException("Unknown operation encountered")

            transaction = TransactionEntity(
                customer_id=account_details.customer_id,
                account_id=account_details.account_id,
                amount=amount,
                txn_type=transaction_type
            )
            self.transaction_repository.save_transaction(transaction)
        except Exception as exception:
            raise ErrorHandlingUtils.application_error("Transaction failed", exception)
