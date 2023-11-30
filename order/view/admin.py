from rest_framework import viewsets

from order.models import Order, OrderDetail
from order.serializers.admin import OrderSerializer, OrderDetailSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
