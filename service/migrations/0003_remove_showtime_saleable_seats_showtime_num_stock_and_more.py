# Generated by Django 4.2.7 on 2023-11-20 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_showtime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='showtime',
            name='saleable_seats',
        ),
        migrations.AddField(
            model_name='showtime',
            name='num_stock',
            field=models.PositiveIntegerField(default=0, verbose_name='صندلی های قابل فروش'),
        ),
        migrations.AddField(
            model_name='showtime',
            name='price',
            field=models.PositiveBigIntegerField(default='1'),
            preserve_default=False,
        ),
    ]
