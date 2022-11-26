from rest_framework.serializers import ModelSerializer

from .models import Advert, Number, Image


class AdvertSerializer(ModelSerializer):
    class Meta:
        model = Advert
        fields = "__all__"


class NumberSerializer(ModelSerializer):
    class Meta:
        model = Number
        fields = ["number"]


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ["image"]
