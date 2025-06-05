import pytest
from src.main import Product, Smartphone, LawnGrass, Category


def test_product_creation():
    product = Product("Товар", "Описание товара", 100.0, 10)
    assert product.name == "Товар"
    assert product.description == "Описание товара"
    assert product.price == 100.0
    assert product.quantity == 10


def test_product_str():
    product = Product("Товар", "Описание товара", 100.0, 10)
    assert str(product) == "Товар, 100.0 руб. Остаток: 10 шт."


def test_product_repr():
    product = Product("Товар", "Описание товара", 100.0, 10)
    assert (
        repr(product)
        == "Product(name='Товар', description='Описание товара', price=100.0, quantity=10)"
    )


def test_smartphone_creation():
    smartphone = Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, "A16", "15", "512GB", "Gray"
    )
    assert smartphone.name == "Iphone 15"
    assert smartphone.performance == "A16"
    assert smartphone.memory == "512GB"


def test_smartphone_repr():
    smartphone = Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, "A16", "15", "512GB", "Gray"
    )
    expected_repr = (
        "Product(name='Iphone 15', description='512GB, Gray space', price=210000.0, quantity=8, "
        "performance='A16', model='15', memory='512GB', color='Gray')"
    )
    assert repr(smartphone) == expected_repr


def test_lawn_grass_creation():
    lawn_grass = LawnGrass(
        "Газонная трава",
        "Для футбольных полей",
        5000.0,
        14,
        "Россия",
        "14 дней",
        "Зеленый",
    )
    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.country == "Россия"


def test_lawn_grass_repr():
    lawn_grass = LawnGrass(
        "Газонная трава",
        "Для футбольных полей",
        5000.0,
        14,
        "Россия",
        "14 дней",
        "Зеленый",
    )
    expected_repr = (
        "Product(name='Газонная трава', description='Для футбольных полей', price=5000.0, quantity=14, "
        "country='Россия', germination_period='14 дней', color='Зеленый')"
    )
    assert repr(lawn_grass) == expected_repr


def test_category_creation():
    product1 = Product("Товар1", "Описание товара1", 100.0, 10)
    product2 = Product("Товар2", "Описание товара2", 200.0, 5)
    category = Category("Техника", "Электронные устройства", [product1, product2])

    assert category.name == "Техника"
    assert category.description == "Электронные устройства"
    assert len(category) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_category_repr():
    product1 = Product("Товар1", "Описание товара1", 100.0, 10)
    category = Category("Техника", "Электронные устройства", [product1])
    expected_repr = "Category(name='Техника', description='Электронные устройства', products=[Product(name='Товар1', description='Описание товара1', price=100.0, quantity=10)])"
    assert repr(category) == expected_repr
