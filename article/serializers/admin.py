from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from article.models import ArticleCategory, Article, ArticleImage, ArticleComment
from media.serializers import ImageSerializer
from user.serializers.admin import UserAdminSerializer


class ArticleCategoryAdminSerializer(serializers.ModelSerializer):
    picture = ImageSerializer(read_only=True, many=True)

    class Meta:
        model = ArticleCategory
        exclude = ('slug',)


class ArticleAdminSerializer(serializers.ModelSerializer):
    authors = UserAdminSerializer(read_only=True, many=True)
    category = ArticleCategoryAdminSerializer(read_only=True, many=True)

    class Meta:
        model = Article
        exclude = ('slug',)


class ArticleImageAdminSerializer(serializers.ModelSerializer):
    images = ArticleAdminSerializer(read_only=True, many=True)
    pictures = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = ArticleImage
        fields = '__all__'


class ArticleCommentAdminSerializer(serializers.ModelSerializer):
    users = UserAdminSerializer(read_only=True, many=True)
    articles = ArticleAdminSerializer(many=True, read_only=True)

    class Meta:
        model = ArticleComment
        fields = '__all__'
