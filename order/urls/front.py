from rest_framework.routers import SimpleRouter

from order.view.front import OrderFrontViewSet, OrderDetailFrontViewSet

router = SimpleRouter()
router.register('order', OrderFrontViewSet)
router.register('orderDetail', OrderDetailFrontViewSet)

urlpatterns = [] + router.urls
