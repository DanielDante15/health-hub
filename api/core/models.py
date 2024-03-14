from django.db import models
from django.contrib.auth.models import AbstractUser

class Personal(AbstractUser):
    crp = models.CharField(max_length=20)
    salario = models.DecimalField(max_digits=10, decimal_places=2)

class Cliente(AbstractUser):
    treinador = models.ForeignKey(Personal, on_delete=models.CASCADE)
    
