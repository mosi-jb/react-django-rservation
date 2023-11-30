from rest_framework.routers import SimpleRouter

from order.view.admin import OrderViewSet, OrderDetailViewSet

router = SimpleRouter()
router.register('order', OrderViewSet)
router.register('orderDetail', OrderDetailViewSet)

urlpatterns = [] + router.urls
