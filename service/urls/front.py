from rest_framework.routers import SimpleRouter

from service.views.front import ServiceViewSet, TimeViewSet, ImageViewSet

router = SimpleRouter()
router.register('ServicesImage', ImageViewSet)
router.register('ShowTime', TimeViewSet)
router.register('Services', ServiceViewSet)

urlpatterns = [] + router.urls
