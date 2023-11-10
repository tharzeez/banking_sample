from src.domain.customer_entity import CustomerEntity


class CustomerRepository:
    def __init__(self):
        self.customers = []

    def save_customer(self, customer: CustomerEntity) -> None:
        self.customers.append(customer)
