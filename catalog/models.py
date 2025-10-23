from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.CharField(max_length=150, verbose_name="Описание")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование",
        help_text="Введите наименование",
    )
    description = models.CharField(
        max_length=150,
        verbose_name="Описание",
        help_text="Введите описание",
    )
    image = models.ImageField(
        upload_to="product/image",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите название категории",
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.IntegerField(
        verbose_name="Цена за покупку",
        help_text="Введите цену",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
        verbose_name="Дата создания",
        help_text="Введите дату создания",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True,
        verbose_name="Дата последнего изменения",
        help_text="Введите последнего изменения",
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Статус публикации",
        help_text="Отметьте, если продукт опубликован",
    )
    owner = models.ForeignKey(
        User,
        verbose_name="Владелец",
        help_text="Укажите владельца товара",
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category"]
        permissions = [
            ("can_unpublish_product", "can unpublish product")
        ]

    def __str__(self):
        return self.name
