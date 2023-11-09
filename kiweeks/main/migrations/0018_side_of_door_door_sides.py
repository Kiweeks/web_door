# Generated by Django 4.2.5 on 2023-11-03 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_category_door_urls'),
    ]

    operations = [
        migrations.CreateModel(
            name='Side_of_door',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sides', models.CharField(max_length=15, verbose_name='Сторона')),
            ],
            options={
                'verbose_name': 'Сторона',
                'verbose_name_plural': 'Стороны',
            },
        ),
        migrations.AddField(
            model_name='door',
            name='sides',
            field=models.ManyToManyField(null=True, related_name='sides_of_doors', to='main.side_of_door'),
        ),
    ]
