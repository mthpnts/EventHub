# Generated by Django 3.0.4 on 2020-05-03 16:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Home', '0019_auto_20200501_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='interested',
            field=models.ManyToManyField(blank=True, help_text='who is interested', related_name='interested', to=settings.AUTH_USER_MODEL),
        ),
    ]