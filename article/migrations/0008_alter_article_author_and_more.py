# Generated by Django 4.2.3 on 2023-12-05 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('media', '0001_initial'),
        ('article', '0007_alter_articlecomment_article_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده'),
        ),
        migrations.AlterField(
            model_name='article',
            name='selected_categories',
            field=models.ManyToManyField(related_name='article', to='article.articlecategory', verbose_name='دسته بندی ها'),
        ),
        migrations.AlterField(
            model_name='articlecategory',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='media.image'),
        ),
    ]
