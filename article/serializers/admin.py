from rest_framework import serializers

from article.models import ArticleCategory
from media.serializers import ImageSerializer


class ArticleCategoryAdminSerializer(serializers.ModelSerializer):
    picture = ImageSerializer(read_only=True, many=True)

    class Meta:
        model = ArticleCategory
        exclude = ('slug',)
