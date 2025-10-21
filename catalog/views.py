from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.forms import ProductForm
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


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("products:products_list")


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("products:products_list")

    def get_success_url(self):
        return reverse("products:product", args=[self.kwargs.get("pk")])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("products:products_list")
