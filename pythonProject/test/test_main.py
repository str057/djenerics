import unittest
from src.main import Product, Smartphone, LawnGrass, Category


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product1 = Product("Товар 1", "Описание товара 1", 100.0, 10)
        self.product2 = Product("Товар 2", "Описание товара 2", 200.0, 5)
        self.smartphone = Smartphone(
            "Samsung Galaxy S23", "Описание", 100000.0, 5, 95.0, "S23", 256, "Серый"
        )

    def test_addition_same_type(self):
        self.assertEqual(self.product1 + self.product2, 300.0)

    def test_addition_different_type(self):
        with self.assertRaises(TypeError):
            self.product1 + self.smartphone


class TestSmartphone(unittest.TestCase):
    def setUp(self):
        self.smartphone = Smartphone(
            "Samsung Galaxy S23", "Описание", 100000.0, 5, 95.0, "S23", 256, "Серый"
        )

    def test_smartphone_attributes(self):
        self.assertEqual(self.smartphone.name, "Samsung Galaxy S23")
        self.assertEqual(self.smartphone.description, "Описание")
        self.assertEqual(self.smartphone.price, 100000.0)
        self.assertEqual(self.smartphone.quantity, 5)
        self.assertEqual(self.smartphone.efficiency, 95.0)
        self.assertEqual(self.smartphone.model, "S23")
        self.assertEqual(self.smartphone.memory, 256)
        self.assertEqual(self.smartphone.color, "Серый")

    def test_smartphone_addition(self):
        smartphone2 = Smartphone(
            "iPhone 15", "Описание", 120000.0, 3, 97.0, "15", 512, "Черный"
        )
        self.assertEqual(self.smartphone + smartphone2, 220000.0)


class TestLawnGrass(unittest.TestCase):
    def setUp(self):
        self.grass = LawnGrass(
            "Газонная трава", "Описание", 500.0, 20, "Россия", "7 дней", "Зеленый"
        )

    def test_lawn_grass_attributes(self):
        self.assertEqual(self.grass.name, "Газонная трава")
        self.assertEqual(self.grass.description, "Описание")
        self.assertEqual(self.grass.price, 500.0)
        self.assertEqual(self.grass.quantity, 20)
        self.assertEqual(self.grass.country, "Россия")
        self.assertEqual(self.grass.germination_period, "7 дней")
        self.assertEqual(self.grass.color, "Зеленый")

    def test_lawn_grass_addition(self):
        grass2 = LawnGrass(
            "Премиум трава", "Описание", 700.0, 15, "Германия", "5 дней", "Изумрудный"
        )
        self.assertEqual(self.grass + grass2, 1200.0)


class TestCategory(unittest.TestCase):
    def setUp(self):
        Category.product_count = 0  # Сбрасываем счетчик перед каждым тестом
        self.category = Category("Смартфоны", "Описание категории")
        self.smartphone = Smartphone(
            "Samsung Galaxy S23", "Описание", 100000.0, 5, 95.0, "S23", 256, "Серый"
        )
        self.grass = LawnGrass(
            "Газонная трава", "Описание", 500.0, 20, "Россия", "7 дней", "Зеленый"
        )

    def test_add_product(self):
        initial_count = Category.product_count
        self.category.add_product(self.smartphone)
        self.assertIn(self.smartphone, self.category.products)
        self.assertEqual(Category.product_count, initial_count + 1)

    def test_add_invalid_product(self):
        with self.assertRaises(TypeError):
            self.category.add_product("Не продукт")

    def test_product_count(self):
        self.assertEqual(Category.product_count, 0)
        self.category.add_product(self.smartphone)
        self.assertEqual(Category.product_count, 1)

        # Создаем новую категорию с продуктами
        new_category = Category("Газоны", "Описание", [self.grass])
        self.assertEqual(Category.product_count, 2)

    def test_initial_products(self):
        category = Category("Тест", "Описание", [self.smartphone, self.grass])
        self.assertEqual(len(category.products), 2)
        self.assertEqual(Category.product_count, 2)


if __name__ == "__main__":
    unittest.main()
