# Generated by Django 5.0.6 on 2024-05-18 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_author_post_cover_alt_post_cover_square_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='cover_alt',
        ),
        migrations.RemoveField(
            model_name='post',
            name='cover_square',
        ),
    ]
