# Generated by Django 4.0.3 on 2022-04-07 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0002_rename_rating_type_ratingmodel_is_liked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingmodel',
            name='is_liked',
            field=models.BooleanField(verbose_name='is liked'),
        ),
    ]
