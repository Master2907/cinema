# Generated by Django 4.0.3 on 2022-04-12 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0031_remove_filmmodel_dislikes_remove_filmmodel_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmmodel',
            name='age',
            field=models.CharField(choices=[('6+', '6+'), ('8+', '8+'), ('12+', '12+'), ('16+', '16+'), ('18+', '18+')], max_length=3, verbose_name='age'),
        ),
    ]
