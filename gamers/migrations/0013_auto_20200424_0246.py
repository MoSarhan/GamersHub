# Generated by Django 2.1.5 on 2020-04-24 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamers', '0012_auto_20200424_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='users',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='game_users', to='gamers.Gamer_ID'),
        ),
    ]
