from datetime import datetime
from django.db import models
from django.conf import settings
from django.contrib.auth import models as authModels
from django.core import validators

# Create your models here.
class User(authModels.AbstractUser):
    birthdate = models.DateField(null=True)
    class Mood(models.IntegerChoices):
        SHORT = 0, 'Short'
        LONG = 1, 'Long'
        ADVENTUROUS = 2, 'Adventurous'
        IMPROVE = 3, 'Improve'
        LUCKY = 4, 'Lucky'
    mood = models.IntegerField(choices=Mood.choices, default=4)
    pass


class Category(models.Model):
    name = models.CharField(max_length=128)
    users_interested = models.ManyToManyField(
        settings.AUTH_USER_MODEL, through="UserInterest", related_name="interests")

    def __str__(self):
        return "%s" % (self.name)


class Tag(models.Model):
    name = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="tags")

    def __str__(self):
        return "%s:%s" % (self.category, self.name)


class Simpleskill(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()

    prerequisites = models.ManyToManyField("self", through="Prerequisite")
    users_registered = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="registered_simpleskills", through="RegisteredSimpleskill")
    user_feedback = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="simpleskills_feedback", through="Feedback")

    tags = models.ManyToManyField(Tag, related_name="simpleskills")

    class Level(models.IntegerChoices):
        BEGINNER = 0, 'Beginner'
        INTERMEDIATE = 1, 'Intermediate'
        ADVANCED = 2, 'Advanced'
    level = models.IntegerField(choices=Level.choices)

    class TimeClass(models.IntegerChoices):
        SHORT = 0, 'Short'
        MEDIUM = 1, 'Medium'
        LONG = 2, 'Long'
    time_class = models.IntegerField(choices=TimeClass.choices)

    def __str__(self):
        return "%s" % (self.name)


class Prerequisite(models.Model):
    from_simpleskill = models.ForeignKey(
        Simpleskill, related_name="pre", on_delete=models.CASCADE)
    to_simpleskill = models.ForeignKey(
        Simpleskill, related_name="next", on_delete=models.CASCADE)

    def __str__(self):
        return "%s is a prerequisite to %s" % (self.from_simpleskill, self.to_simpleskill)

    class Importance(models.IntegerChoices):
        LOW = 0, 'Low',
        MEDIUM = 1, 'Medium',
        HIGH = 2, 'High'
    importance = models.IntegerField(choices=Importance.choices)


class UserInterest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    interest_level = models.IntegerField(default=0, validators=[
                                         validators.MinValueValidator(0), validators.MaxValueValidator(100)])

    class Level(models.IntegerChoices):
        BEGINNER = 0, 'Beginner'
        INTERMEDIATE = 1, 'Intermediate'
        ADVANCED = 2, 'Advanced'
    experience_level = models.IntegerField(choices=Level.choices, default=0)
    def __str__(self):
        return "%s->%s:%d" % (self.user, self.category, self.experience_level)


class Feedback(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                             on_delete=models.SET_NULL)
    simpleskill = models.ForeignKey(Simpleskill, null=True,
                                    on_delete=models.CASCADE)
    quality_vote = models.BooleanField()
    enjoyment_vote = models.BooleanField()
    date_collected = models.DateField()


class Milestone(models.Model):
    name = models.CharField(max_length=128)
    simpleskill = models.ForeignKey(Simpleskill, on_delete=models.CASCADE, related_name="milestones")
    description = models.TextField(null=True)

    def __str__(self):
        return "%s:%s:%s" % (self.simpleskill, self.name, self.description)


class Material(models.Model):
    name = models.CharField(max_length=128)
    title = models.CharField(max_length=256, null=True)
    description = models.TextField(null=True)
    milestone = models.ForeignKey(Milestone, on_delete=models.CASCADE, related_name="materials")
    url = models.URLField()

    class MaterialType(models.IntegerChoices):
        ARTICLE = 0, 'Article'
        VIDEO = 1, 'Video'
        PROJECT = 2, 'Project'
    type = models.IntegerField(choices=MaterialType.choices)

    def __str__(self):
        return "%s:%s:%s" % (self.milestone, self.name, self.description)


class RegisteredSimpleskill(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    simpleskill = models.ForeignKey(Simpleskill, on_delete=models.CASCADE)

    finished_materials = models.ManyToManyField(Material, null=True)

    date_started = models.DateTimeField(default=datetime.now, blank=True)
