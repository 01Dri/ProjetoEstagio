from repository.productrepository import ProductRepository
from entities.product import Product

class ProductService:

    def __init__(self) -> None:
        self.product_repository = ProductRepository()
    

    def save_product(self, data):
        product_dto = Product(**data)
        return self.product_repository.save_product(product_dto)

    def find_all_products(self):
        return self.product_repository.find_all_products()
