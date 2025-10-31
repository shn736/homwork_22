from django.core.cache import cache

from catalog.models import Product
from config.settings import CASH_ENABLED


def get_products_from_cache():
    """Получает данные продукта из кэша, если кэш пуст, получает данные из бд."""
    if not CASH_ENABLED:
        return Product.objects.all()
    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


def get_products_by_category(category_id):
    """Возвращает список продуктов в указанной категории."""
    return Product.objects.filter(category_id=category_id)
