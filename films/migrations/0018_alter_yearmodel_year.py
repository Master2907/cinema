# Generated by Django 4.0.3 on 2022-03-29 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0017_alter_yearmodel_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yearmodel',
            name='year',
            field=models.PositiveIntegerField(default=2022, unique=True, verbose_name='year'),
        ),
    ]