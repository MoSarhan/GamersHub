# Generated by Django 2.1.5 on 2020-04-24 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamers', '0009_auto_20200424_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend_request',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_request_status', to='gamers.Gamer_ID'),
        ),
    ]
