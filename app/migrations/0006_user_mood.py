# Generated by Django 4.0.4 on 2022-05-22 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_userinterest_experience_level_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mood',
            field=models.IntegerField(choices=[(0, 'Short'), (1, 'Long'), (2, 'Adventurous'), (3, 'Improve'), (4, 'Lucky')], default=4),
        ),
    ]
