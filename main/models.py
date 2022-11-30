from django.db import models
from cloudinary.models import CloudinaryField


class Advert(models.Model):

    items = (
        ("1", "К.Мүлк"),
        ("2", "Авто"),
        ("3", "Мал чарба"),
        ("4", "Алуу сатуу"),
        ("5", "Жумуш"),
        ("6", "Электроника"),
        ("7", "Каттам"),

    )

    author = models.CharField(max_length=50, verbose_name="Автор")
    itemchoice = models.CharField(
        max_length=50, default="New Item", choices=items)
    description = models.TextField(verbose_name="Описание")
    whatsapp_number = models.CharField(
        max_length=15, verbose_name="Номер телефона(whatsApp)")
    add_date = models.DateTimeField(
        auto_now=True, verbose_name="Дата добавление")

    def __str__(self):
        return f"Реклама - {self.author}"

    class Meta:
        verbose_name = "Реклама"
        verbose_name_plural = "Рекламы"


class Number(models.Model):
    advert = models.ForeignKey(
        to=Advert, on_delete=models.CASCADE, related_name="my_numbers")
    number = models.CharField(max_length=15, verbose_name="Номер телефона")

    def __str__(self):
        return f"{self.advert} - {self.number}"

    class Meta:
        verbose_name = "Номер"
        verbose_name_plural = "Номера"


class Image(models.Model):
    advert = models.ForeignKey(
        to=Advert, on_delete=models.CASCADE, related_name="my_images")
    image = CloudinaryField("images")

    def __str__(self):
        return f"Фото - {self.advert}"

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"
