from django.contrib import admin

from service.models import Services, ShowTime, ServicesImage


# Register your models here.


class ProductAttributeValueInline(admin.StackedInline):
    model = ShowTime
    extra = 2


class ProductImageInline(admin.StackedInline):
    model = ServicesImage
    extra = 2


@admin.register(Services)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    inlines = [ProductAttributeValueInline, ProductImageInline, ]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(ShowTime)
admin.site.register(ServicesImage)
