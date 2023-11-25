from rest_framework import viewsets

from article.models import ArticleCategory
from article.serializers.admin import ArticleCategorySerializer


class ArticleCategoryViewSet(viewsets.ModelViewSet):
    queryset = ArticleCategory.objects.all()
    serializer_class = ArticleCategorySerializer
