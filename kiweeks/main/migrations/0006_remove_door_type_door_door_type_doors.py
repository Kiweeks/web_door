# Generated by Django 4.2.5 on 2023-10-26 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_type_door_alter_door_type_door'),
    ]

    operations = [
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
