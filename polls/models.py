from django.db import models

# Create your models here.

class Collaborator(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)

class UserTest(models.Model):
  collaborator = models.ForeignKey(Collaborator, on_delete=models.CASCADE, default=1)
  password = models.CharField(max_length=30, default="contraseña")
  username = models.CharField(max_length=10, default="usuario")