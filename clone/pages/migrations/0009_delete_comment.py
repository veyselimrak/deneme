# Generated by Django 4.1.4 on 2022-12-27 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_remove_comment_create_at_remove_comment_ip_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
