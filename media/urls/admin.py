from rest_framework.routers import SimpleRouter

from media.view.admin import ImageViewSet

router = SimpleRouter()
router.register('Image', ImageViewSet)

urlpatterns = [] + router.urls
