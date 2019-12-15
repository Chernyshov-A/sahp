# Generated by Django 2.2.6 on 2019-12-13 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_remove_history_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='user',
            field=models.ForeignKey(default='8', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]