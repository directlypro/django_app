from django.db import models

# Create your models here.
class Users(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    join_date = models.DateField(null=True)