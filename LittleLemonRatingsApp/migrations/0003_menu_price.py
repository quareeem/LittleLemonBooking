# Generated by Django 4.1.2 on 2023-04-10 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonRatingsApp', '0002_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='price',
            field=models.IntegerField(default=98),
            preserve_default=False,
        ),
    ]