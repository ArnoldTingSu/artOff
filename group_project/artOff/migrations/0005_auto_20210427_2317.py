# Generated by Django 2.2 on 2021-04-28 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artOff', '0004_auto_20210427_2311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='art',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='art',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='updated_at',
        ),
    ]