# Generated by Django 4.2.5 on 2023-11-24 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_door_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='door',
            name='colors_outside',
            field=models.ManyToManyField(null=True, related_name='color_outside', to='main.color_outside'),
        ),
        migrations.AlterField(
            model_name='door',
            name='sides',
            field=models.ManyToManyField(related_name='sides_of_doors', to='main.side_of_door'),
        ),
        migrations.AlterField(
            model_name='door',
            name='sizes',
            field=models.ManyToManyField(related_name='size_doors', to='main.size_door'),
        ),
    ]