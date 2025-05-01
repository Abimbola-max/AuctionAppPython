from abc import ABC, abstractmethod

from src.data.models.product import Product
from src.data.models.productphase import ProductPhase


class ProductInterface(ABC):

    @abstractmethod
    def create_product(self, product: Product) -> Product:
        pass

    @abstractmethod
    def find_product(self, product_id: str) -> Product:
        pass

    @abstractmethod
    def update_product(self, product_id, product):
        pass

    @abstractmethod
    def update_product_status(self, product_id: str, phase:  ProductPhase):
        pass

    @abstractmethod
    def update_product_price(self, product_id, current_price):
        pass
