from rest_framework import serializers
from admin_app.models import Resume
from company_app.models import Company
from vacancy_app.models import Application, Vacancy, Specialty


class ResumeSerializer(serializers.ModelSerializer):
    """
    Serializing all the Resumes
    """

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Resume
        fields = ('id', 'name', 'surname', 'status', 'salary', 'grade',
                  'education', 'experience', 'specialty', 'user', 'portfolio')


class CompanySerializer(serializers.ModelSerializer):
    """
    Serializing all the Companies
    """
    class Meta:
        model = Company
        fields = ('id', 'name', 'location', 'description', 'employee_count', 'owner_id',
                  'logo')


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
