from django.db import models

# Create your models here.

class account_module(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email=models.EmailField()
    class Meta:
        db_table='account_table'