# Generated by Django 2.1.5 on 2020-04-21 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamers', '0002_gamer_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='gamer',
            name='bio',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AlterField(
            model_name='gamer',
            name='pp',
            field=models.ImageField(blank=True, upload_to='pp/'),
        ),
        migrations.AddField(
            model_name='game',
            name='plateforms',
            field=models.ManyToManyField(to='gamers.Platform'),
        ),
        migrations.AddField(
            model_name='gamer',
            name='games',
            field=models.ManyToManyField(to='gamers.Game'),
        ),
    ]
