from rest_framework import viewsets
from service.models import Services, ShowTime, ServicesImage
from service.serializers.front import ServiceSerializer, TimeSerializer, ImageSerializers


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer


class TimeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ShowTime.objects.all()
    serializer_class = TimeSerializer


class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ServicesImage.objects.all()
    serializer_class = ImageSerializers
