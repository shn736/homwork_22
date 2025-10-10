from django.db import models


class Blogs(models.Model):
    header = models.CharField(
        max_length=150,
        verbose_name="Заголовок",
        help_text="Введите наименование заголовка",
    )
    content = models.CharField(
        max_length=150, verbose_name="Содержимое", help_text="Введите содержимое"
    )

    preview = models.ImageField(
        upload_to="blogs/image",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите превью",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
        verbose_name="Дата создания",
        help_text="Введите дату создания",
    )

    publication_attribute = models.BooleanField(default=False)

    number_of_views = models.PositiveIntegerField(
        verbose_name="Число просмотров", help_text="Введите число просмотров", default=0
    )

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"

    def __str__(self):
        return self.header
