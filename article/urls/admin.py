from rest_framework.routers import SimpleRouter

from article.view.admin import ArticleCategoryAdminViewSet

router = SimpleRouter()
router.register('articlecategory', ArticleCategoryAdminViewSet)

urlpatterns = [] + router.urls
