from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, products_list, product

app_name = CatalogConfig.name

urlpatterns = [
    path('', products_list, name="products_list"),
    path('products/<int:pk>', product, name="product"),
]
