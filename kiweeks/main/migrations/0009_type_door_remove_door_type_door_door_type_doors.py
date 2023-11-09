# Generated by Django 4.2.5 on 2023-10-26 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_door_type_doors_door_type_door_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type_door',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_doors', models.CharField(max_length=100, verbose_name='Тип двери')),
            ],
            options={
                'verbose_name': 'Тип двери',
                'verbose_name_plural': 'Типы дверей',
            },
        ),
        migrations.RemoveField(
            model_name='door',
            name='type_door',
        ),
        migrations.AddField(
            model_name='door',
            name='type_doors',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.type_door'),
        ),
    ]
