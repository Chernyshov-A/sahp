# Generated by Django 2.2.6 on 2019-12-14 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20191213_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='name',
            field=models.CharField(default='Без названия', max_length=200),
        ),
    ]