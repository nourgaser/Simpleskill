# Generated by Django 4.0.4 on 2022-04-21 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_simpleskill_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeredsimpleskill',
            name='finished_materials',
            field=models.ManyToManyField(to='app.material'),
        ),
    ]
