# Generated by Django 5.1.6 on 2025-02-17 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=256),
        ),
    ]
