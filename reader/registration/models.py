from django.db import models


class UsersData(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250, default=None)
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=100)
