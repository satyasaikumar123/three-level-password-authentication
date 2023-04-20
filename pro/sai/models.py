from django.db import models

# Create your models here.

class CustomUser(models.Model):
    email = models.EmailField(unique=True)
    color = models.CharField(max_length=20)
