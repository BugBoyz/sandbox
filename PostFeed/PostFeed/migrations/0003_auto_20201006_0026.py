# Generated by Django 3.1.1 on 2020-10-05 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostFeed', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=32),
        ),
    ]
