from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(
        upload_to="catalog/",
        blank=True,
        null=True,
        verbose_name="Изображение (превью)",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Категория",
        related_name="categories",
    )
    price = models.FloatField(verbose_name="Цена за покупку")
    creation_at = models.DateTimeField(default=timezone.now, verbose_name="Дата создания (записи в БД)")
    updated_at = models.DateTimeField(default=timezone.now, verbose_name="Дата последнего изменения (записи в БД)"
                                      )

    def __str__(self):
        return f'{self.name} {self.price}'

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
