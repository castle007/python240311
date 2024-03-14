from openpyxl import Workbook
from random import randint

def generate_product_data(num_products):
    products = []
    for i in range(1, num_products + 1):
        product_id = i
        product_name = f"Product {i}"
        product_price = randint(10, 1000)  # 임의의 가격 생성 (10에서 1000 사이의 값)
        products.append((product_id, product_name, product_price))
    return products

def save_to_excel(filename, data):
    wb = Workbook()
    ws = wb.active
    ws.append(["제품ID", "제품이름", "제품가격"])
    for product in data:
        ws.append(product)
    wb.save(filename)

# 데이터 생성
product_data = generate_product_data(100)

# 엑셀 파일로 저장
save_to_excel("products.xlsx", product_data)

print("데이터가 성공적으로 생성되고 products.xlsx 파일에 저장되었습니다.")
