from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=20)
    id = models.CharField(max_length=20, primary_key=True)
    pw =  models.CharField(max_length=20)

class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    context = models.CharField()