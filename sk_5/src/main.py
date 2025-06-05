from abc import ABC, abstractmethod


class LogMixin:
    def __init__(self, *args, **kwargs):
        print(f"Создан объект класса {self.__class__.__name__} с параметрами:")
        for arg in args:
            print(f"- {arg}")
        for key, value in kwargs.items():
            print(f"- {key}: {value}")
        super().__init__(*args, **kwargs)

    def __repr__(self):
        params = ", ".join([f"{key}={value!r}" for key, value in self.__dict__.items()])
        return f"{self.__class__.__name__}({params})"


class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class Product(BaseProduct, LogMixin):
    def __init__(self, name, description, price, quantity):
        super().__init__(
            name=name, description=description, price=price, quantity=quantity
        )

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        return f"Product(name={self.name!r}, description={self.description!r}, price={self.price!r}, quantity={self.quantity!r})"


class Smartphone(Product):
    def __init__(
        self, name, description, price, quantity, performance, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color

    def __repr__(self):
        base_repr = super().__repr__()[:-1]  # Убираем закрывающую скобку
        return f"{base_repr}, performance={self.performance!r}, model={self.model!r}, memory={self.memory!r}, color={self.color!r})"


class LawnGrass(Product):
    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __repr__(self):
        base_repr = super().__repr__()[:-1]  # Убираем закрывающую скобку
        return f"{base_repr}, country={self.country!r}, germination_period={self.germination_period!r}, color={self.color!r})"


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self):
        return self.__products

    def __len__(self):
        return len(self.__products)

    def __repr__(self):
        return f"Category(name={self.name!r}, description={self.description!r}, products={self.products!r})"


if __name__ == "__main__":
    # Примеры использования
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, "A16", "15", "512GB", "Gray"
    )
    product3 = LawnGrass(
        "Газонная трава",
        "Для футбольных полей",
        5000.0,
        14,
        "Россия",
        "14 дней",
        "Зеленый",
    )

    print("\nПримеры продуктов:")
    print(product1)  # Использует __str__
    print(repr(product1))  # Использует __repr__
    print(repr(product2))
    print(repr(product3))

    category = Category("Техника", "Электронные устройства", [product1, product2])
    print("\nКатегория:", repr(category))
    print("Всего категорий:", Category.category_count)
    print("Всего продуктов:", Category.product_count)
