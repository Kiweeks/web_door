# Generated by Django 4.2.5 on 2023-10-11 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_door_remove_photo_door_door_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo_door',
            options={'verbose_name': 'Фотография', 'verbose_name_plural': 'Фотографии'},
        ),
    ]
