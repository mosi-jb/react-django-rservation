from rest_framework.routers import SimpleRouter

from service.views.admin import ServiceAdminViewSet, TimeAdminViewSet, ImageAdminViewSet

router = SimpleRouter()
router.register('ServicesImage', ImageAdminViewSet)
router.register('ShowTime', TimeAdminViewSet)
router.register('Services', ServiceAdminViewSet)

urlpatterns = [] + router.urls
