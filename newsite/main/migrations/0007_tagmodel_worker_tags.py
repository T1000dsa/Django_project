# Generated by Django 5.1.6 on 2025-02-18 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_worker_cat'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(db_index=True, max_length=96)),
                ('slug', models.SlugField(max_length=128, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='worker',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='main.tagmodel'),
        ),
    ]
