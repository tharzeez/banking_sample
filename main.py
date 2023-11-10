from src.config.context import BaseContext
from src.domain.app_exception import AppException

ctx = BaseContext()


def test_banking_scenario():
    try:
        account = ctx.account_use_case.create_account(1, name="John", email="john@email.com",
                                                      phone_number="987 623 1234")

        account2 = ctx.account_use_case.create_account(2, name="Alice", email="alice@email.com",
                                                       phone_number="653 623 1234")
        ctx.transaction_use_case.make_transaction(account.account_id, 35, "deposit")
        ctx.transaction_use_case.make_transaction(account.account_id, 10, "withdraw")
        ctx.transaction_use_case.make_transaction(account.account_id, 10, "withdraw")

        ctx.transaction_use_case.make_transaction(account2.account_id, 35, "deposit")
        ctx.transaction_use_case.make_transaction(account2.account_id, 45, "withdraw")

    except AppException as e:
        print(f"An application error occurred: {e}")
    except Exception as e:
        # Handle other types of exceptions
        print(f"An unexpected error occurred: {e}")
    finally:
        account_statements = ctx.account_statement_use_case.generate_account_statement(account_id=account.account_id)
        string_list = [
            f"Amount is {statement.amount} type {statement.txn_type} for the customer {statement.customer_id}" for
            statement in account_statements]

        # Join the list of strings into a single string
        result_string = ', \n '.join(string_list)
        print(f"Final statement for account 1 \n {result_string}")

        account_statements = ctx.account_statement_use_case.generate_account_statement(account_id=account2.account_id)
        string_list = [
            f"Amount is {statement.amount} type {statement.txn_type} for the customer {statement.customer_id}" for
            statement in account_statements]

        # Join the list of strings into a single string
        result_string = ', \n '.join(string_list)
        print(f"Final statement for account 2 \n {result_string}")


if __name__ == "__main__":
    test_banking_scenario()
