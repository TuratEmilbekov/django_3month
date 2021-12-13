from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='')


    def __str__(self):
        return f'{self.title}'