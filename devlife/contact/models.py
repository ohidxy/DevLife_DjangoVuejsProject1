from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    hp_no = models.CharField(max_length=128, blank=True)
    twitter = models.URLField(max_length=50, blank=True)
    github = models.URLField(max_length=50, blank=True)
    company = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
