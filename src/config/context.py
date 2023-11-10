from src.adapter.repositories.account_repository import AccountRepository
from src.adapter.repositories.customer_repository import CustomerRepository
from src.adapter.repositories.transaction_repository import TransactionRepository
from src.usecases.account_statements_usecase import AccountStatementUseCase
from src.usecases.account_usecase import AccountUseCase
from src.usecases.transaction_usecase import TransactionUseCase


class BaseContext:
    def __init__(self):
        # Repositories
        self.account_repo = AccountRepository()
        self.customer_repo = CustomerRepository()
        self.txn_repo = TransactionRepository()

        # Use cases
        self.account_use_case = AccountUseCase(self.account_repo, self.customer_repo)
        self.transaction_use_case = TransactionUseCase(self.account_repo, self.txn_repo)
        self.account_statement_use_case = AccountStatementUseCase(self.txn_repo)
