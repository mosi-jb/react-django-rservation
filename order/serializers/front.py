from rest_framework import serializers

from order.models import Order, OrderDetail
from service.serializers.admin import TimeAdminSerializer
from user.serializers.admin import UserAdminSerializer


class OrderFrontSerializer(serializers.ModelSerializer):
    userss = UserAdminSerializer(read_only=True, many=True)

    class Meta:
        model = Order
        fields = '__all__'


class OrderDetailFrontSerializer(serializers.ModelSerializer):
    orderdetail_set = OrderFrontSerializer(read_only=True, many=True)
    sans = TimeAdminSerializer(read_only=True, many=True)

    class Meta:
        model = OrderDetail
        fields = '__all__'
