# Generated by Django 3.2.16 on 2023-03-01 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptions',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
