# Generated by Django 4.0.3 on 2022-04-24 08:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rating', '0004_ratingmodel_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratingmodel',
            name='user',
        ),
        migrations.AddField(
            model_name='ratingmodel',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
