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
        upload_to='media/catalog',
        blank=True,
        null=True,
        verbose_name='Изображение (превью)',
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


class Version(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='Продукт', related_name='version')
    number_version = models.IntegerField(default=1, verbose_name='номер версии')
    name_version = models.CharField(max_length=100, verbose_name='имя версии')
    version_flag = models.BooleanField(default=False, verbose_name='признак версии')

    def __str__(self):
        return f'{self.name_version}'

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
