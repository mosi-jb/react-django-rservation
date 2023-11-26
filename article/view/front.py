from rest_framework import viewsets

from article.models import ArticleCategory, Article, ArticleImage, ArticleComment
from article.serializers.front import ArticleCategorySerializer, ArticleSerializer, ArticleImageSerializer, \
    ArticleCommentSerializer


class ArticleCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ArticleCategory.objects.all()
    serializer_class = ArticleCategorySerializer


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ArticleImage.objects.all()
    serializer_class = ArticleImageSerializer


class ArticleCommentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ArticleComment.objects.all()
    serializer_class = ArticleCommentSerializer
