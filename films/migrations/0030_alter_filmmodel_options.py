# Generated by Django 4.0.3 on 2022-04-06 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0029_alter_filmmodel_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filmmodel',
            options={'verbose_name': 'film', 'verbose_name_plural': 'films'},
        ),
    ]
