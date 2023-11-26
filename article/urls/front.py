from rest_framework.routers import SimpleRouter

from article.view.front import ArticleCategoryViewSet, ArticleViewSet, ArticleImageViewSet, ArticleCommentViewSet

router = SimpleRouter()
router.register('articlecategory', ArticleCategoryViewSet)
router.register('article', ArticleViewSet)
router.register('articleImage', ArticleImageViewSet)
router.register('articleComment', ArticleCommentViewSet)

urlpatterns = [] + router.urls
