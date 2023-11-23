from rest_framework import serializers

from media.serializers import ImageSerializer
from service.models import Services, ShowTime, ServicesImage


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class TimeSerializer(serializers.ModelSerializer):
    showTime = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = ShowTime
        fields = '__all__'


class ImageSerializers(serializers.ModelSerializer):
    images = ServiceSerializer(many=True, read_only=True)
    imagess = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = ServicesImage
        fields = '__all__'
