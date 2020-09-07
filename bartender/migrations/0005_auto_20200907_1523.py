# Generated by Django 3.1.1 on 2020-09-07 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bartender', '0004_drink_timesmade'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='associatedImage',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='drink',
            name='name',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]
