# Generated by Django 2.1.5 on 2020-04-24 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamers', '0022_auto_20200424_0349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend_request',
            name='status',
        ),
    ]
