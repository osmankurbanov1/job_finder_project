# Generated by Django 4.0.2 on 2022-03-19 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('employee_count', models.IntegerField()),
                ('logo', models.URLField(default='https://place-hold.it/100x60')),
            ],
        ),
    ]
