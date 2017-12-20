from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    hp_no = models.CharField(max_length=128)
    twitter = models.URLField()
    github = models.URLField()
    company = models.CharField(max_length=255)
