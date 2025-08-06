from django.core.management.base import BaseCommand
from fly.models import Category, Product


class Command(BaseCommand):
    help = "Load test data with database cleanup"

    def handle(self, *args, **options):
        # Clear existing data
        self.stdout.write("Clearing existing data...")
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Create test categories
        electronics = Category.objects.create(
            name="Electronics", description="Electronic gadgets"
        )
        books = Category.objects.create(name="Books", description="Various books")

        # Create test products
        Product.objects.create(
            name="Smartphone",
            price=599.99,
            category=electronics,
            description="Flagship smartphone",
        )
        Product.objects.create(name="Laptop", price=1299.99, category=electronics)

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully created: "
                f"{Category.objects.count()} categories, "
                f"{Product.objects.count()} products"
            )
        )
