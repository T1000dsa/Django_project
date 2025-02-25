# Generated by Django 5.1.6 on 2025-02-23 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_uploadfiles_alter_worker_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y-%m-%d', verbose_name='Pthot'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='content',
            field=models.TextField(blank=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='slug',
            field=models.SlugField(max_length=256, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='title',
            field=models.CharField(max_length=256, verbose_name='Title'),
        ),
    ]
