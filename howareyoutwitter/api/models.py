from django.db import models

# Create your models here.
class Token(models.Model):
    token_type = models.CharField(max_length=300)
    access_token = models.CharField(max_length=300)