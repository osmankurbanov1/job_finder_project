from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    employee_count = models.IntegerField()
    #logo = models.URLField(default='https://place-hold.it/100x60')
    logo = models.ImageField(upload_to='MEDIA_COMPANY_IMAGE_DIR', null=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='companies', null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.name