# Generated by Django 4.2.5 on 2023-10-30 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_door_размер_door_sizes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo_door',
            name='photos',
            field=models.ImageField(null=True, upload_to='photo_door/', verbose_name='Фото'),
        ),
    ]
