# backend/users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from companies.models import Company    # 👈 importa el modelo desde la otra app

class User(AbstractUser):
    full_name      = models.CharField(max_length=150)
    phone          = models.CharField(max_length=20, blank=True)
    phone_verified = models.BooleanField(default=False)

    # 👇 vuelve a añadir el FK apuntando a companies.Company
    company = models.ForeignKey(
        Company,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="users"
    )

