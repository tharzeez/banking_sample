from abc import ABC, abstractmethod
import typing

from src.domain.customer_entity import CustomerEntity


class CustomerRepositoryAbstract(ABC):
    @abstractmethod
    def save_customer(self, customer_id: int, name: str, email: str, phone_number: str) -> None:
        """Save account"""
