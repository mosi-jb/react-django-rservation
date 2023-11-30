from rest_framework import serializers

from order.models import Order, OrderDetail
from service.serializers.admin import TimeAdminSerializer
from user.serializers.admin import UserAdminSerializer


class OrderSerializer(serializers.ModelSerializer):
    userss = UserAdminSerializer(read_only=True, many=True)

    class Meta:
        model = Order
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    orderdetail_set = OrderSerializer(read_only=True, many=True)
    sans = TimeAdminSerializer(read_only=True, many=True)

    class Meta:
        model = OrderDetail
        fields = '__all__'
