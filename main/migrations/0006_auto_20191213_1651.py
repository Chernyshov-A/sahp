# Generated by Django 2.2.6 on 2019-12-13 16:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20191213_1544'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='create_date',
        ),
        migrations.AddField(
            model_name='history',
            name='selection_add',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]