from rest_framework import serializers

from order.models import Order, OrderDetail


class OrderDetailFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'


class OrderFrontSerializer(serializers.ModelSerializer):
    orderdetail_set = OrderDetailFrontSerializer(read_only=True, many=True)

    class Meta:
        model = Order
        fields = '__all__'
