from rest_framework.routers import SimpleRouter

from article.view.admin import ArticleCategoryAdminViewSet, ArticleAdminViewSet, ArticleImageAdminViewSet, \
    ArticleCommentAdminViewSet
from article.view.front import ArticleImageViewSet

router = SimpleRouter()
router.register('articlecategory', ArticleCategoryAdminViewSet)
router.register('article', ArticleAdminViewSet)
router.register('articleImage', ArticleImageAdminViewSet)
router.register('articleComment', ArticleCommentAdminViewSet)

urlpatterns = [] + router.urls
