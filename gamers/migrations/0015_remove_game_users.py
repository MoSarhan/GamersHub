# Generated by Django 2.1.5 on 2020-04-24 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamers', '0014_auto_20200424_0249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='users',
        ),
    ]