from rest_framework import viewsets

from order.models import Order, OrderDetail
from order.serializers.front import OrderFrontSerializer, OrderDetailFrontSerializer


class OrderFrontViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderFrontSerializer


class OrderDetailFrontViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailFrontSerializer
