# Generated by Django 4.2.7 on 2023-11-20 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_remove_services_cover_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='slug',
            field=models.SlugField(allow_unicode=True, default='t', unique=True),
            preserve_default=False,
        ),
    ]
