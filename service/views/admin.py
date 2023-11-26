from rest_framework import viewsets
from service.models import Services, ShowTime, ServicesImage
from service.serializers.admin import ServiceAdminSerializer, TimeAdminSerializer, ImageAdminSerializers


class ServiceAdminViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServiceAdminSerializer


class TimeAdminViewSet(viewsets.ModelViewSet):
    queryset = ShowTime.objects.all()
    serializer_class = TimeAdminSerializer


class ImageAdminViewSet(viewsets.ModelViewSet):
    queryset = ServicesImage.objects.all()
    serializer_class = ImageAdminSerializers
