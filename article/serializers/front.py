from rest_framework import serializers

from article.models import ArticleCategory, Article, ArticleImage, ArticleComment


class ArticleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleImage
        fields = '__all__'


class ArticleCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleComment
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    comment = ArticleCommentSerializer(read_only=True, many=True)
    images = ArticleImageSerializer(read_only=True, many=True)

    class Meta:
        model = Article
        exclude = ('slug',)


class ArticleCategorySerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=True, many=True)

    class Meta:
        model = ArticleCategory
        exclude = ('slug',)
