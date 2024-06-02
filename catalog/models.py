from django.db import models
from django.utils import timezone

from users.models import User

NULLABLE = {"null": True, "blank": True}


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
    description = models.TextField(verbose_name="Описание", **NULLABLE)
    image = models.ImageField(
        upload_to="media/catalog", verbose_name="Изображение (превью)", **NULLABLE
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
    creation_at = models.DateTimeField(
        default=timezone.now, verbose_name="Дата создания (записи в БД)"
    )
    updated_at = models.DateTimeField(
        default=timezone.now, verbose_name="Дата последнего изменения (записи в БД)"
    )
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, verbose_name="Создан пользователем", **NULLABLE
    )
    is_published = models.BooleanField(default=False, verbose_name="Признак публикации")

    def __str__(self):
        return f"{self.name} {self.price}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        permissions = [
            ("set_published_status", "Can publish product"),
            ("change_description", "Can change product description"),
            ("change_category", "Can change product category"),
        ]


class Version(models.Model):
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        verbose_name="Продукт",
        related_name="version",
    )
    number_version = models.IntegerField(default=1, verbose_name="номер версии")
    name_version = models.CharField(max_length=100, verbose_name="имя версии")
    version_flag = models.BooleanField(default=False, verbose_name="признак версии")

    def __str__(self):
        return f"{self.name_version}"

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
