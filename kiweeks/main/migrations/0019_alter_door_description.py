# Generated by Django 4.2.5 on 2023-11-13 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_side_of_door_door_sides'),
    ]

    operations = [
        migrations.AlterField(
            model_name='door',
            name='description',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
    ]
