from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    employee_count = models.IntegerField()
    logo = models.URLField(default='https://place-hold.it/100x60')

    objects = models.Manager()