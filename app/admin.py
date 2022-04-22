from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.Simpleskill)
admin.site.register(models.Tag)
admin.site.register(models.Prerequisite)
admin.site.register(models.RegisteredSimpleskill)
admin.site.register(models.UserInterest)
admin.site.register(models.Feedback)
admin.site.register(models.Milestone)
admin.site.register(models.Material)
admin.site.register(models.User, UserAdmin)
