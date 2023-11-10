from src.domain.base_entity import BaseEntity


class CustomerEntity(BaseEntity):
    def __init__(self, customer_id: int, name: str, email: str,
                 phone_number: str) -> None:
        super().__init__()
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone_number = phone_number
