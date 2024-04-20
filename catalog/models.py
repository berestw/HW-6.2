from django.db import models


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
        upload_to="catalog/preview",
        blank=True,
        null=True,
        verbose_name="Изображение (превью)",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Категория",
        related_name="categories",
    )
    price = models.IntegerField(verbose_name="Цена за покупку")
    creation_at = models.DateTimeField(verbose_name="Дата создания (записи в БД)")
    updated_at = models.DateTimeField(
        verbose_name="Дата последнего изменения (записи в БД)"
    )
    manufactured_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Дата производства продукта"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category", "price"]
