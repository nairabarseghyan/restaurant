# Generated by Django 3.1 on 2020-09-07 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(blank=True, max_length=100, null=True)),
                ('food_photo', models.ImageField(blank=True, default='profile_pics/log.jpg', upload_to='foods')),
            ],
        ),
    ]