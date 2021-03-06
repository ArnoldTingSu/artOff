# Generated by Django 2.2 on 2021-04-28 06:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('artOff', '0003_auto_20210427_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='art',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
