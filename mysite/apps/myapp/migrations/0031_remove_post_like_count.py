# Generated by Django 4.0.4 on 2022-05-30 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0030_post_like_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='like_count',
        ),
    ]