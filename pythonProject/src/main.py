class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product")
        return self.price * self.quantity + other.price * other.quantity

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return (
            self.name == other.name
            and self.price == other.price
            and self.quantity == other.quantity
        )


class Category:
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.products)
        product_list = "\n".join(str(product) for product in self.products)
        return (
            f"Категория: {self.name}\n"
            f"Описание: {self.description}\n"
            f"Количество продуктов: {total_quantity} шт.\n"
            f"Список продуктов:\n{product_list}"
        )


if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    print("\n" + str(category1))

    print("\nСуммарная стоимость товаров:")
    print(f"{product1.name} + {product2.name} = {product1 + product2} руб.")
    print(f"{product1.name} + {product3.name} = {product1 + product3} руб.")
    print(f"{product2.name} + {product3.name} = {product2 + product3} руб.")
