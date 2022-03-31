from django.db import models
from django.contrib.auth.models import User
from vacancy_app.models import Specialty

# Create your models here.


class Resume(models.Model):
    objects = models.Manager()

    NO = 'N'
    MAYBE = 'M'
    YES = 'Y'
    JOB_STATUS_CHOICES = [
        (NO, 'Не ищу работу'),
        (MAYBE, 'Рассматриваю предложения'),
        (YES, 'Ищу работу'),
    ]

    INTERN = 'IN'
    JUNIOR = 'JU'
    MIDDLE = 'MI'
    SENIOR = 'SE'
    LEAD = 'LE'
    GRADES_CHOICES = [
        (INTERN, 'Стажер'),
        (JUNIOR, 'Джуниор'),
        (MIDDLE, 'Миддл'),
        (SENIOR, 'Синьор'),
        (LEAD, 'Лид'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="resumes")
    name = models.CharField(max_length=10)
    surname = models.CharField(max_length=10)
    status = models.CharField(
        max_length=1,
        choices=JOB_STATUS_CHOICES,
        default=MAYBE,
    )
    salary = models.IntegerField()
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="resumes")
    grade = models.CharField(
        max_length=2,
        choices=GRADES_CHOICES,
        default=INTERN,
    )
    education = models.TextField()
    experience = models.TextField()
    portfolio = models.URLField()

