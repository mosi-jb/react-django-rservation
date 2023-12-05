from django.db import models


class Services(models.Model):
    title = models.CharField(max_length=128, verbose_name='عنوان')
    url_title = models.CharField(max_length=200, unique=True, verbose_name='عنوان در url')
    price = models.BigIntegerField(verbose_name='قیمت')
    slug = models.SlugField(unique=True, allow_unicode=True)

    @property
    def main_image(self):
        if self.images.exists():
            return self.images.first()
        else:
            return None

    class Meta:
        verbose_name = 'خدمات'
        verbose_name_plural = 'خدمات ها'

    def __str__(self):
        return self.title


class ShowTime(models.Model):
    Services = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='showTime')
    start_time = models.DateTimeField(verbose_name='تاریخ شروع')
    end_time = models.DateTimeField(verbose_name='تاریخ پایان ')
    price = models.PositiveBigIntegerField()
    num_stock = models.PositiveIntegerField(default=0, verbose_name='صندلی های قابل فروش')

    class Meta:
        verbose_name = 'سانس'
        verbose_name_plural = 'سانس ها'

    def __str__(self):
        return '{} - {}'.format(self.Services, self.start_time)


class ServicesImage(models.Model):
    product = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='images')
    image = models.ForeignKey('media.Image', on_delete=models.PROTECT, verbose_name='تصویر')

    display_order = models.PositiveIntegerField(default=0, verbose_name='ترتیب')

    class Meta:
        ordering = ('display_order',)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

        for index, image in enumerate(self.product.images.all()):
            image.display_order = index
            image.save()
