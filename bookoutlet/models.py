from django.db import models

# Create your models here.

class Books(models.Model):
    """New Book class"""
    title = models.CharField(max_length=50)
    ratings = models.IntegerField()
    
    