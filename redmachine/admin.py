from django.contrib import admin
from django.db import models
from . import models

# Register your models here.
admin.site.register(models.Car)
admin.site.register(models.CommentCar)