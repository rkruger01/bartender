# Generated by Django 3.1.1 on 2020-09-07 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bartender', '0003_auto_20200907_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='timesMade',
            field=models.IntegerField(default=0),
        ),
    ]
