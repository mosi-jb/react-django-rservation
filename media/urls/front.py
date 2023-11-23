from rest_framework.routers import SimpleRouter

from media.view.front import ImageViewSet

router = SimpleRouter()
router.register('Image', ImageViewSet)

urlpatterns = [] + router.urls
