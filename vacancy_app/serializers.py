from rest_framework import serializers
from .models import Vacancy, Specialty, Application


class ApplicationSerializer(serializers.ModelSerializer):
    """
    Serializing all the Applications
    """

    class Meta:
        model = Application
        fields = ('id', 'written_username', 'written_phone', 'written_cover_letter', 'vacancy')


class VacancyRelatedCompanySerializer(serializers.ModelSerializer):
    """
    Serializing the Vacancies related to Company
    """

    applications = ApplicationSerializer(read_only=True, many=True)

    class Meta:
        model = Vacancy
        fields = ('id', 'title', 'skills', 'description', 'posted', 'salary_from',
                  'salary_to', 'specialty', 'applications')


class VacancySerializer(serializers.ModelSerializer):
    """
    Serializing all the Vacancies
    """

    applications = ApplicationSerializer(read_only=True, many=True)

    class Meta:
        model = Vacancy
        fields = ('id', 'title', 'skills', 'description', 'salary_from',
                  'salary_to', 'specialty', 'applications')


class SpecialtySerializer(serializers.ModelSerializer):
    """
    Serializing all the Specialities
    """

    class Meta:
        model = Specialty
        fields = ('id', 'code', 'title', 'logo')
