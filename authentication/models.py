from django.db import models

from django.contrib.auth.models import User


# class CustomUser(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE) 
#     phoneno = models.CharField(max_length=10, default='7795518387')

class ExtentedUser(models.Model):
    user_data = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneno = models.CharField(max_length=10)
    