from rest_framework import viewsets

from media.models import Image
from media.serializers import ImageSerializer


class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
