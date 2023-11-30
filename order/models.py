from django.db import models


# Create your models here.


class Order(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, verbose_name='کاربر', related_name='userss')
    is_paid = models.BooleanField(verbose_name='نهایی شده/نشده')
    payment_date = models.DateField(null=True, blank=True, verbose_name='تاریخ پرداخت')

    def __str__(self):
        return str(self.user)

    def calculate_total_price(self):
        total_amount = 0
        if self.is_paid:
            for order_detail in self.orderdetail_set.all():
                total_amount += order_detail.product.price
        else:
            for order_detail in self.orderdetail_set.all():
                total_amount += order_detail.product.price

        return total_amount

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبدهای خرید کاربران'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید', related_name='orderdetail_set')
    product = models.ForeignKey("service.ShowTime", on_delete=models.CASCADE, verbose_name='سانس', related_name='sans')

    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name = 'جزییات سبد خرید'
        verbose_name_plural = 'لیست جزییات سبدهای خرید'
