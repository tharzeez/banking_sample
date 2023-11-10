from src.utils.number_utils import random_number
from src.utils.error_handling_utils import ErrorHandlingUtils
from src.domain.account_entity import AccountEntity
from src.domain.customer_entity import CustomerEntity
from src.application.repositories.account_repository_abstract import AccountRepositoryAbstract
from src.application.repositories.customer_repository_abstract import CustomerRepositoryAbstract


class AccountUseCase:
    def __init__(self,
                 account_repository: AccountRepositoryAbstract,
                 customer_repository: CustomerRepositoryAbstract
                 ) -> None:
        self.account_repository = account_repository
        self.customer_repository = customer_repository

    def create_account(self, customer_id, name, email, phone_number) -> AccountEntity:
        try:
            customer = CustomerEntity(customer_id, name, email, phone_number)
            total_accounts_count = self.account_repository.get_accounts_count()
            account = AccountEntity(account_id=total_accounts_count+1,
                                    customer_id=customer_id,
                                    account_number=random_number(16)
                                    )
            self.customer_repository.save_customer(customer)
            self.account_repository.save_account(account)
            return account
        except Exception as exception:
            raise ErrorHandlingUtils.application_error("Account creation failed", exception)
