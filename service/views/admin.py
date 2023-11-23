from rest_framework import viewsets
from service.models import Services, ShowTime, ServicesImage
from service.serializers.admin import ServiceSerializer, TimeSerializer, ImageSerializers


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer


class TimeViewSet(viewsets.ModelViewSet):
    queryset = ShowTime.objects.all()
    serializer_class = TimeSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = ServicesImage.objects.all()
    serializer_class = ImageSerializers
