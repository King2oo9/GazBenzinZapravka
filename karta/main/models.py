from django.db import models


# Create your models here.

class Gaz(models.Model):
    nomi = models.CharField(max_length=120)
    manzili = models.CharField(max_length=120)
    narx = models.CharField(max_length=120)


class Benzin(models.Model):
    nomi = models.CharField(max_length=120)
    manzili = models.CharField(max_length=120)
    narx = models.CharField(max_length=120)
