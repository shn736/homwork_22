from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="products_list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product"),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path("blogs/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("blogs/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
]
