from django.db import models


class Kino(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    graduationYear = models.IntegerField()
    image = models.ImageField(upload_to='app1/image')
    linkToView = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

    
# Create your models here.
