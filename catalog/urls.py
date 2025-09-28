from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name="products_list"),
    path('products/<int:pk>', ProductDetailView.as_view(), name="product"),
]
