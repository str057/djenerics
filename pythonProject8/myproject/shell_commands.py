from fly.models import Category, Product

# 1. Создание категорий
cat1 = Category.objects.create(name="Электроника", description="Гаджеты")
cat2 = Category.objects.create(name="Книги", description="Литература")
print("Созданы категории:", cat1, cat2)

# 2. Создание продуктов
p1 = Product.objects.create(name="Смартфон", price=599.99, category=cat1)
p2 = Product.objects.create(name="Ноутбук", price=1299.99, category=cat1)
p3 = Product.objects.create(name="Python для начинающих", price=29.99, category=cat2)
print("Созданы продукты:", p1, p2, p3)

# 3. Вывод всех данных
print("\nВсе категории:", list(Category.objects.all()))
print("Все продукты:", list(Product.objects.all()))