from django.db import models
from django.contrib.auth.models import User

from company_app.models import Company

# Create your models here.


class Specialty(models.Model):

    code = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='MEDIA_SPECIALITY_IMAGE_DIR', null=True)

    objects = models.Manager()

    def __str__(self):
        return f'{self.title}'


class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    skills = models.TextField()
    description = models.TextField()
    posted = models.DateField()
    salary_from = models.IntegerField()
    salary_to = models.IntegerField()
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")

    objects = models.Manager()

    def __str__(self):
        return self.title


class Application(models.Model):
    written_username = models.CharField(max_length=20)
    written_phone = models.CharField(max_length=20)
    written_cover_letter = models.TextField(null=True)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='applications', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications', null=True)

    objects = models.Manager()

    def __str__(self):
        return f'Application from {self.written_username}'
