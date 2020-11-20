from django.db import models

# Create your models here.
class product(models.Model):
    title = models.CharField(max_lenght=200)
    desc = models.CharField(max_length=300)