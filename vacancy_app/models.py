from django.db import models
from company_app.models import Company
# Create your models here.


class Specialty(models.Model):

    code = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    objects = models.Manager()


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
