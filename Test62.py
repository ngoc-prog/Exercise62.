from MODULE3.Exercise62.models.Category import Category
from MODULE3.Exercise62.models.Product import Product


def display_categories(categories):
    print("Danh sách danh mục của cửa hàng:")
    for category in categories:
        print(category)


def update_product_in_category(category, product_id, **kwargs):
    print(f"\nUpdating product {product_id}:")
    print(category.update_product(product_id, **kwargs))


def delete_product_in_category(category, product_id):
    print(f"\nDeleting product {product_id}:")
    print(category.delete_product(product_id))


def calculate_total_value_for_category(category):
    print(f"\nCalculating total value for category {category.id}:")
    print(f"Total value: {category.calculate_total_value()}")


if __name__ == "__main__":
    c1 = Category("C1", "Thuốc")
    c2 = Category("C2", "Nước ngọt")
    c3 = Category("C3", "Bia")

    c1.add_product(Product("P1", "Thuốc trị ghẻ", 15, "Trung Quốc"))
    c1.add_product(Product("P2", "Thuốc trị phong bạt", 20, "Hồng Kong"))

    c2.add_product(Product("P3", "Nước khoáng lavie", 22, "Việt Nam"))
    c2.add_product(Product("P4", "Nước suối bà Tám", 12, "Việt Nam"))
    c2.add_product(Product("P5", "Nước dừa bà Bảy", 23, "Việt Nam"))

    c3.add_product(Product("P6", "Bia Hồng Lâu Mộng", 10, "Trung Quốc"))

    categories = [c1, c2, c3]

    display_categories(categories)

    print("\nDanh sách sản phẩm phân loại theo danh mục:")
    for category in categories:
        print("*" * 30)
        print(category)
        print("*" * 30)
        category.print_products()

    update_product_in_category(c1, "P1", name="Thuốc trị ghẻ updated", price=18)
    delete_product_in_category(c2, "P4")
    calculate_total_value_for_category(c2)

    print("\nFiltering products from Việt Nam in category C2:")
    vietnam_products = c2.filter_by_origin("Việt Nam")
    for product in vietnam_products:
        print(product)