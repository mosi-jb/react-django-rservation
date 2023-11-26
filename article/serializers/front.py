from rest_framework import serializers

from article.models import ArticleCategory, Article, ArticleImage, ArticleComment
from article.serializers.admin import ArticleAdminSerializer
from media.serializers import ImageSerializer
from user.serializers.admin import UserAdminSerializer


class ArticleCategorySerializer(serializers.ModelSerializer):
    picture = ImageSerializer(read_only=True, many=True)

    class Meta:
        model = ArticleCategory
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    authors = UserAdminSerializer(read_only=True, many=True)
    category = ArticleCategorySerializer(read_only=True, many=True)

    class Meta:
        model = Article
        exclude = ('slug',)


class ArticleImageSerializer(serializers.ModelSerializer):
    images = ArticleSerializer(read_only=True, many=True)
    pictures = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = ArticleImage
        fields = '__all__'


class ArticleCommentSerializer(serializers.ModelSerializer):
    users = UserAdminSerializer(read_only=True, many=True)
    articles = ArticleAdminSerializer(many=True, read_only=True)

    class Meta:
        model = ArticleComment
        fields = '__all__'

