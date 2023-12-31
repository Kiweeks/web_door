# Generated by Django 4.2.5 on 2023-10-27 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_type_door_remove_door_type_door_door_type_doors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size_door',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sizes_doors', models.CharField(max_length=25, verbose_name='Размер')),
            ],
            options={
                'verbose_name': 'Размер',
                'verbose_name_plural': 'Размеры',
            },
        ),
        migrations.RemoveField(
            model_name='door',
            name='style',
        ),
        migrations.AlterField(
            model_name='door',
            name='colors_outside',
            field=models.ManyToManyField(related_name='color_outside', to='main.color_outside'),
        ),
        migrations.AddField(
            model_name='door',
            name='sizes',
            field=models.ManyToManyField(null=True, related_name='size_doors', to='main.size_door'),
        ),
    ]
