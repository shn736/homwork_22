from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Add test products to the database"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()
        category, _ = Category.objects.get_or_create(name="Продукты")

        products = [
            {
                "name": "Сосиски",
                "description": "Продукты питания",
                "price": 50,
                "category": category,
            },
            {
                "name": "Колбаса",
                "description": "Продукты питания",
                "price": 50,
                "category": category,
            },
            {
                "name": "Мясо",
                "description": "Продукты питания",
                "price": 50,
                "category": category,
            },
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully added product: {product.name}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Product already exists: {product.name}")
                )
