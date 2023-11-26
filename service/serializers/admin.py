from rest_framework import serializers

from media.serializers import ImageSerializer
from service.models import Services, ShowTime, ServicesImage


class ServiceAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class TimeAdminSerializer(serializers.ModelSerializer):
    showTime = ServiceAdminSerializer(many=True, read_only=True)

    class Meta:
        model = ShowTime
        fields = '__all__'


class ImageAdminSerializers(serializers.ModelSerializer):
    images = ServiceAdminSerializer(many=True, read_only=True)
    imagess = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = ServicesImage
        fields = '__all__'
