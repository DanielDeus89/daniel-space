# Generated by Django 5.1.3 on 2024-12-08 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_fotografia_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='publicadas',
            field=models.BooleanField(default=False),
        ),
    ]