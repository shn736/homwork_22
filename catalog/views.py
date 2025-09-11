from django.shortcuts import render


def home(request):
    """Контроллер рендерит шаблон главной страницы функцией"""
    return render(request, '../templates/catalogs/home.html')


def contacts(request):
    """Контроллер рендерит шаблон страницы контактов функцией"""
    return render(request, '../templates/catalogs/contacts.html')
