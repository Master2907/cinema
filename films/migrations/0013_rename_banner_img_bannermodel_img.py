# Generated by Django 4.0.3 on 2022-03-25 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0012_alter_filmmodel_age_alter_filmmodel_movie_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bannermodel',
            old_name='banner_img',
            new_name='img',
        ),
    ]
