from rest_framework import serializers

from service.models import Services, ShowTime, ServicesImage


class TimeAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowTime
        fields = '__all__'


class ImageAdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = ServicesImage
        fields = '__all__'


class ServiceAdminSerializer(serializers.ModelSerializer):
    showTime = TimeAdminSerializer(read_only=True, many=True)
    images = ImageAdminSerializers(read_only=True, many=True)

    class Meta:
        model = Services
        fields = '__all__'
