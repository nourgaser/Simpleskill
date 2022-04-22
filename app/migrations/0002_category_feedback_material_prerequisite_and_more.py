# Generated by Django 4.0.4 on 2022-04-22 17:35

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality_vote', models.BooleanField()),
                ('enjoyment_vote', models.BooleanField()),
                ('date_collected', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('type', models.IntegerField(choices=[(0, 'Article'), (1, 'Video'), (2, 'Project')])),
            ],
        ),
        migrations.CreateModel(
            name='Prerequisite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('importance', models.IntegerField(choices=[(0, 'Low'), (1, 'Medium'), (2, 'High')])),
            ],
        ),
        migrations.CreateModel(
            name='RegisteredSimpleskill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_started', models.DateField()),
                ('finished_materials', models.ManyToManyField(to='app.material')),
            ],
        ),
        migrations.CreateModel(
            name='UserInterest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest_level', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('experience_level', models.IntegerField(choices=[(0, 'Beginner'), (1, 'Intermediate'), (2, 'Advanced')])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Simpleskill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('level', models.IntegerField(choices=[(0, 'Beginner'), (1, 'Intermediate'), (2, 'Advanced')])),
                ('time_class', models.IntegerField(choices=[(0, 'Short'), (1, 'Medium'), (2, 'Long')])),
                ('prerequisites', models.ManyToManyField(through='app.Prerequisite', to='app.simpleskill')),
                ('tags', models.ManyToManyField(to='app.tag')),
                ('user_feedback', models.ManyToManyField(related_name='simpleskills_feedback', through='app.Feedback', to=settings.AUTH_USER_MODEL)),
                ('users_registered', models.ManyToManyField(related_name='registered_simpleskills', through='app.RegisteredSimpleskill', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='registeredsimpleskill',
            name='simpleskill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.simpleskill'),
        ),
        migrations.AddField(
            model_name='registeredsimpleskill',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='prerequisite',
            name='from_simpleskill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pre', to='app.simpleskill'),
        ),
        migrations.AddField(
            model_name='prerequisite',
            name='to_simpleskill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='next', to='app.simpleskill'),
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('simpleskill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.simpleskill')),
            ],
        ),
        migrations.AddField(
            model_name='material',
            name='milestone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.milestone'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='simpleskill',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.simpleskill'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='category',
            name='users_interested',
            field=models.ManyToManyField(through='app.UserInterest', to=settings.AUTH_USER_MODEL),
        ),
    ]