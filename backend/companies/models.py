# companies/models.py
from django.db import models

class Company(models.Model):
    name        = models.CharField(max_length=200)
    logo        = models.ImageField(upload_to='logos/', blank=True, null=True)
    size        = models.CharField(max_length=100)      # e.g. "51–200 empleados"
    industry    = models.CharField(max_length=100)      # e.g. "Automotriz"
    location    = models.CharField(max_length=200)      # sede principal
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
