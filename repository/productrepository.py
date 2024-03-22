import sqlite3
from entities.product import Product
from typing import List

class ProductRepository:

    def __init__(self) -> None:
        self.conn = sqlite3.connect('products.db')
        self.cursor = self.conn.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            value REAL NOT NULL,
            isAvailable BOOLEAN NOT NULL
        )
        """
        self.cursor.execute(create_table_query)
        self.conn.commit()

    def find_all_products(self) -> List[Product]:
        products = []

        query = "SELECT * FROM products WHERE isAvailable = 1"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        for row in rows:
            product = Product(
                name=row[1],
                description=row[2],
                value=row[3],
                isAvailable=row[4]
            )
            products.append(product)

        return products
        
    def save_product(self, product: Product):
        query = """
        INSERT INTO products (name, description, value, isAvailable)
        VALUES (?, ?, ?, ?)
        """
        values = (product.name, product.description, product.value, product.isAvailable)
        self.cursor.execute(query, values)

        self.conn.commit()

        return True

    def __del__(self):
        self.cursor.close()
        self.conn.close()
