from django.contrib import admin
from django.urls import path

from main.views import AdvertListAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adverts/', AdvertListAPIView.as_view(), name="adverts"),
]
