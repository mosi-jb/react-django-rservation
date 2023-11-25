from django.contrib import admin
from django.http import HttpRequest

from article.models import Article, ArticleCategory, ArticleComment, ArticleImage


# Register your models here.


class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title', 'is_active']
    list_editable = ['url_title', 'is_active']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'author']
    list_editable = ['is_active']

    def save_model(self, request: HttpRequest, obj: Article, form, change):
        if not change:
            obj.author = request.user
        return super().save_model(request, obj, form, change)


class ArticleInline(admin.StackedInline):
    model = ArticleImage
    extra = 2


@admin.register(Article)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    inlines = [ArticleInline]
    prepopulated_fields = {"slug": ("title",)}


class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'create_date', ]


admin.site.register(ArticleCategory, ArticleCategoryAdmin)
# admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleComment, ArticleCommentAdmin)
