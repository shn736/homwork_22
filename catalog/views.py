from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from catalog.models import Product


def home(request):
    """Контроллер рендерит шаблон главной страницы функцией"""
    return render(request, "../templates/catalog/home.html")


def contacts(request):
    """Контроллер рендерит шаблон страницы контактов функцией"""
    return render(request, "../templates/catalog/contacts.html")


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product
# def product(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {"product": product}
#     return render(request, '../templates/catalog/product_detail.html', context)
