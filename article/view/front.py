from rest_framework import viewsets

from article.models import ArticleCategory
from article.serializers.front import ArticleCategorySerializer


class ArticleCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ArticleCategory.objects.all()
    serializer_class = ArticleCategorySerializer
