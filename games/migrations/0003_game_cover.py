# Generated by Django 3.1.14 on 2021-12-27 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers/'),
        ),
    ]