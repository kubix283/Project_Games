# Generated by Django 3.1.14 on 2021-12-27 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_game_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'permissions': [('special_status', 'Can play all games')]},
        ),
    ]