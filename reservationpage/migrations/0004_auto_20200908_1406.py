# Generated by Django 3.1 on 2020-09-08 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservationpage', '0003_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='bill',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='time',
            field=models.CharField(default='DEFAULT VALUE', max_length=2),
        ),
    ]