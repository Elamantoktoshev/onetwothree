from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from main import models, serializers


class AdvertListAPIView(ListAPIView):
    queryset = models.Advert.objects.all()
    serializer_class = serializers.AdvertSerializer

    def list(self, request, *args, **kwargs):
        adverts, result = models.Advert.objects.all(), []
        for advert in adverts:
            nums = serializers.NumberSerializer(
                advert.my_numbers.all(), many=True)
            # ims = serializers.ImageSerializer(
            #     advert.my_images.all(), many=True)
            ims = serializers.ImageSerializer(
                advert.my_images.all(), many=True)
            ser = dict(self.serializer_class(advert).data)
            ser.update(numbers=nums.data)
            ser.update(ims=ims.data)
            result.append(ser)
        return Response(result, status=200)
