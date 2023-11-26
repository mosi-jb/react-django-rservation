from rest_framework import viewsets

from article.models import ArticleCategory, Article, ArticleImage, ArticleComment
from article.serializers.admin import ArticleCategoryAdminSerializer, ArticleAdminSerializer, \
    ArticleImageAdminSerializer, ArticleCommentAdminSerializer


class ArticleCategoryAdminViewSet(viewsets.ModelViewSet):
    queryset = ArticleCategory.objects.all()
    serializer_class = ArticleCategoryAdminSerializer


class ArticleAdminViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleAdminSerializer


class ArticleImageAdminViewSet(viewsets.ModelViewSet):
    queryset = ArticleImage.objects.all()
    serializer_class = ArticleImageAdminSerializer


class ArticleCommentAdminViewSet(viewsets.ModelViewSet):
    queryset = ArticleComment.objects.all()
    serializer_class = ArticleCommentAdminSerializer
