# Generated by Django 4.0.4 on 2022-05-23 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_material_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='title',
            field=models.CharField(max_length=256, null=True),
        ),
    ]