# Generated by Django 4.0.2 on 2022-03-28 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy_app', '0002_specialty_logo_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='written_cover_letter',
            field=models.TextField(null=True),
        ),
    ]
