from rest_framework.routers import SimpleRouter

from article.view.admin import ArticleCategoryViewSet

router = SimpleRouter()
router.register('articlecategory', ArticleCategoryViewSet)

urlpatterns = [] + router.urls
