# Generated by Django 4.0.3 on 2022-04-07 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ratingmodel',
            old_name='rating_type',
            new_name='is_liked',
        ),
    ]
