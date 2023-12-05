from rest_framework import serializers

from service.models import Services, ShowTime, ServicesImage


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowTime
        fields = '__all__'


class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ServicesImage
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    showTime = TimeSerializer(read_only=True, many=True)
    images = ImageSerializers(read_only=True, many=True)

    class Meta:
        model = Services
        fields = '__all__'
