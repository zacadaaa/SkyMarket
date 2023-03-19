from django.conf import settings
from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название товара", null=True)
    price = models.PositiveIntegerField(verbose_name="Цена", null=True)
    description = models.CharField(blank=True, null=True, max_length=1000, verbose_name="Описание товара")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор", null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата объявления", null=True)
    image = models.ImageField(upload_to='ad_images', verbose_name="фото", blank=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


class Comment(models.Model):
    text = models.CharField(max_length=1000, verbose_name="Комментарий", null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                               verbose_name="Автор комментария", null=True)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name="Объявление", null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата комментария", null=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
