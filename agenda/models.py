from django.db import models

# Create your models here.
class Compromisso(models.Model):
    titulo = models.CharField(max_length=15)
    data = models.DateTimeField()
    descricao = models.TextField()

