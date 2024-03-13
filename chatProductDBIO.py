import sqlite3
import random
import string

class ProductManager:
    def __init__(self, db_name='products.db'):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS products (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            price REAL
                            )''')
        self.conn.commit()

    def insert_product(self, id, name, price):
        self.cur.execute("INSERT INTO products (id, name, price) VALUES (?, ?, ?)", (id, name, price))
        self.conn.commit()

    def update_product_price(self, id, new_price):
        self.cur.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, id))
        self.conn.commit()

    def delete_product(self, id):
        self.cur.execute("DELETE FROM products WHERE id = ?", (id,))
        self.conn.commit()

    def select_all_products(self):
        self.cur.execute("SELECT * FROM products")
        return self.cur.fetchall()

    def generate_random_products(self, num_products):
        for _ in range(num_products):
            id = random.randint(100000, 999999)  # 랜덤한 6자리 숫자 ID 생성
            name = ''.join(random.choices(string.ascii_letters, k=random.randint(5, 10)))
            price = round(random.uniform(10, 1000), 2)
            self.insert_product(id, name, price)

if __name__ == "__main__":
    pm = ProductManager()
    pm.generate_random_products(100)

    print("전체 제품 목록:")
    products = pm.select_all_products()
    for product in products:
        print(product)
