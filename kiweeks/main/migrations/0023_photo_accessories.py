# Generated by Django 5.0 on 2023-12-26 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_alter_category_door_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo_accessories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photo_accessories/', verbose_name='Фото фурнитура')),
            ],
            options={
                'verbose_name': 'Фурнитура',
                'verbose_name_plural': 'Фурнитура',
            },
        ),
    ]
