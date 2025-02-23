# Generated by Django 5.1.6 on 2025-02-19 06:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_tagmodel_worker_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Helmet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('helmet_name', models.CharField(default='Helmet', max_length=64, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='worker',
            name='helmet',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='worhel', to='main.helmet'),
        ),
    ]
