from django.db import models

# Create your models here.

class Zapravka(models.Model):
    nomi = models.CharField(max_length=120)
    manzili = models.CharField(max_length=120)
    turi = models.CharField(max_length=120)