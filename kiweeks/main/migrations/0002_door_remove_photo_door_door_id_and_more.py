# Generated by Django 4.2.5 on 2023-10-11 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Door',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('brand', models.CharField(max_length=255, verbose_name='Бренд')),
                ('style', models.CharField(max_length=50, verbose_name='Стиль')),
                ('type_door', models.CharField(max_length=100, verbose_name='Тип')),
                ('properties', models.TextField(verbose_name='Характеристики')),
                ('description', models.TextField(verbose_name='Описание')),
                ('colors_inside', models.ManyToManyField(related_name='color_inside', to='main.color_inside')),
                ('colors_outside', models.ManyToManyField(related_name='color_inside', to='main.color_outside')),
            ],
            options={
                'verbose_name': 'Дверь',
                'verbose_name_plural': 'Двери',
            },
        ),
        migrations.RemoveField(
            model_name='photo_door',
            name='door_id',
        ),
        migrations.AlterField(
            model_name='photo_door',
            name='photos',
            field=models.ImageField(null=True, upload_to='', verbose_name='Фото'),
        ),
        migrations.DeleteModel(
            name='Doors',
        ),
        migrations.AddField(
            model_name='photo_door',
            name='doors',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.door'),
        ),
    ]
