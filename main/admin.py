from django.contrib import admin

from .models import Advert, Image, Number


class ImageTabular(admin.TabularInline):
    model = Image
    extra = 0


class NumberTabular(admin.TabularInline):
    model = Number
    extra = 0


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ["author", "whatsapp_number", "add_date"]
    inlines = [ImageTabular, NumberTabular]
    save_on_top = True