from rest_framework import serializers

from article.models import ArticleCategory, Article, ArticleImage, ArticleComment


class ArticleImageAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleImage
        fields = '__all__'


class ArticleCommentAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleComment
        fields = '__all__'


class ArticleAdminSerializer(serializers.ModelSerializer):
    comment = ArticleCommentAdminSerializer(read_only=True, many=True)
    images = ArticleImageAdminSerializer(read_only=True, many=True)

    class Meta:
        model = Article
        exclude = ('slug',)


class ArticleCategoryAdminSerializer(serializers.ModelSerializer):
    article = ArticleAdminSerializer(read_only=True, many=True)

    class Meta:
        model = ArticleCategory
        exclude = ('slug',)
