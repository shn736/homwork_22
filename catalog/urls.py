from django.urls import path
from django.views.decorators.cache import cache_page
from catalog.apps import CatalogConfig
from catalog.views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    CategoryProductListView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="products_list"),
    path(
        "products/<int:pk>/",
        cache_page(60)(ProductDetailView.as_view()),
        name="product",
    ),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path(
        "products/<int:category_id>/category_products/",
        CategoryProductListView.as_view(),
        name="category_products",
    ),
    path("blogs/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("blogs/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
]
