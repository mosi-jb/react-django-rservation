from rest_framework import viewsets

from article.models import ArticleCategory
from article.serializers.admin import ArticleCategoryAdminSerializer


class ArticleCategoryAdminViewSet(viewsets.ModelViewSet):
    queryset = ArticleCategory.objects.all()
    serializer_class = ArticleCategoryAdminSerializer
