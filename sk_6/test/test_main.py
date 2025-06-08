import pytest
from src.main import Product, Category


def test_product_zero_quantity():
    with pytest.raises(ValueError) as excinfo:
        Product("Test", "Test", 100, 0)
    assert "Товар с нулевым количеством не может быть добавлен" in str(excinfo.value)


def test_middle_price_with_products():
    product1 = Product("Product1", "Desc1", 100, 1)
    product2 = Product("Product2", "Desc2", 200, 2)
    category = Category("Test", "Test", [product1, product2])
    assert category.middle_price() == 150


def test_middle_price_empty_category():
    category = Category("Test", "Test", [])
    assert category.middle_price() == 0


def test_middle_price_single_product():
    product = Product("Product", "Desc", 100, 1)
    category = Category("Test", "Test", [product])
    assert category.middle_price() == 100
