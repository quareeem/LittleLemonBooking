# Generated by Django 4.1.2 on 2023-04-08 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonRatingsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('reservation_date', models.DateField()),
                ('reservation_slot', models.SmallIntegerField(default=10)),
            ],
        ),
    ]
