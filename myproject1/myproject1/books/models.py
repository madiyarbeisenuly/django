from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    author = models.CharField(max_length=100, verbose_name="Автор")
    description = models.TextField(blank=True, verbose_name="Описание")
    cover = models.ImageField(upload_to='book_covers/', blank=True, null=True, verbose_name="Обложка")

    def __str__(self):
        return self.title