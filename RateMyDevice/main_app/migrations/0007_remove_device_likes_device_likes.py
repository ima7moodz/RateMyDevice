# Generated by Django 5.1.5 on 2025-02-15 14:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_message'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='likes',
        ),
        migrations.AddField(
            model_name='device',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_devices', to=settings.AUTH_USER_MODEL),
        ),
    ]
