from django.db import models


class Advert(models.Model):
    author = models.CharField(max_length=50, verbose_name="Автор")
    description = models.TextField(verbose_name="Описание")
    whatsapp_number = models.CharField(max_length=15, verbose_name="Номер телефона(whatsapp)")
    add_date = models.DateTimeField(auto_now=True, verbose_name="Дата добавление")

    def __str__(self):
        return f"Реклама - {self.author}"

    class Meta:
        verbose_name = "Реклама"
        verbose_name_plural = "Рекламы"


class Number(models.Model):
    advert = models.ForeignKey(to=Advert, on_delete=models.CASCADE, related_name="my_numbers")
    number = models.CharField(max_length=15, verbose_name="Номер телефона")

    def __str__(self):
        return f"{self.advert} - {self.number}"

    class Meta:
        verbose_name = "Номер"
        verbose_name_plural = "Номера"


class Image(models.Model):
    advert = models.ForeignKey(to=Advert, on_delete=models.CASCADE, related_name="my_images")
    image = models.ImageField(upload_to="images/", verbose_name="Фото")

    def __str__(self):
        return f"Фото - {self.advert}"

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"



