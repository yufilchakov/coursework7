# Generated by Django 5.1.2 on 2024-10-15 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='is_public',
            field=models.BooleanField(default=True, verbose_name='Публичная'),
        ),
    ]
