# Generated by Django 2.1.5 on 2020-04-21 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamers', '0004_auto_20200421_0155'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='abbreviation',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
