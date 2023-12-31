# Generated by Django 4.2.7 on 2023-11-20 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
        ('service', '0006_rename_productimage_servicesimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicesimage',
            name='display_order',
            field=models.PositiveIntegerField(default=0, verbose_name='ترتیب'),
        ),
        migrations.AlterField(
            model_name='servicesimage',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='media.image', verbose_name='تصویر'),
        ),
    ]
