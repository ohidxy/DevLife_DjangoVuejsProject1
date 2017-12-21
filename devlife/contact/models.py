from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    hp_no = models.CharField(max_length=128)
    twitter = models.URLField()
    github = models.URLField()
    company = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
