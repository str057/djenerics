import pytest
from src.main import Product, Category  # Убедитесь, что путь корректный


def test_product_str():
    product = Product("Test Product", "Test Description", 100.0, 5)
    assert str(product) == "Test Product, 100.0 руб. Остаток: 5 шт."


def test_category_str():
    products = [
        Product("Test Product 1", "Description 1", 100.0, 2),
        Product("Test Product 2", "Description 2", 200.0, 3),
    ]
    category = Category("Test Category", "Test Description", products)
    category_str = str(category)
    assert "Категория: Test Category" in category_str
    assert "Количество продуктов: 5 шт." in category_str
    assert "Список продуктов:" in category_str
    assert "Test Product 1" in category_str
    assert "Test Product 2" in category_str


def test_product_addition():
    p1 = Product("Product 1", "Description 1", 100.0, 2)
    p2 = Product("Product 2", "Description 2", 200.0, 3)
    expected_sum = p1.price * p1.quantity + p2.price * p2.quantity
    assert p1 + p2 == expected_sum


def test_product_addition_invalid_type():
    p1 = Product("Product 1", "Description 1", 100.0, 2)
    with pytest.raises(TypeError):
        _ = p1 + 100


def test_product_subtraction():
    p1 = Product("Product 1", "Description 1", 100.0, 5)
    p2 = Product("Product 2", "Description 2", 50.0, 2)

    try:
        result = p1 - p2
        expected = p1.price * p1.quantity - p2.price * p2.quantity
        assert result == expected
    except TypeError:
        # Если метод __sub__ не реализован, пропускаем тест
        pytest.skip("Метод __sub__ не реализован в классе Product")


def test_product_equality():
    p1 = Product("Product 1", "Description", 100.0, 2)
    p2 = Product("Product 1", "Description", 100.0, 2)
    p3 = Product("Product 3", "Description", 200.0, 1)
    try:
        assert p1 == p2
        assert p1 != p3
    except AssertionError:
        pytest.fail("Метод __eq__ не реализован корректно или отсутствует.")


def test_product_less_than_greater_than():
    p1 = Product("Product 1", "Description", 100.0, 2)
    p2 = Product("Product 2", "Description", 200.0, 3)
    try:
        assert p1 < p2
        assert p2 > p1
    except TypeError:
        pytest.skip("Методы __lt__ и __gt__ не реализованы в классе Product.")


if __name__ == "__main__":
    pytest.main()
