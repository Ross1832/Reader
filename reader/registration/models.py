from django.db import models


class RegistrationData(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=100)
    registration_date = models.DateField(auto_now=True)
