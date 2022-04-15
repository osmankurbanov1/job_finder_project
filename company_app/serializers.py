from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    """
    Serializing all the Companies
    """
    class Meta:
        model = Company
        fields = ('id', 'name', 'location', 'description', 'employee_count', 'owner_id',
                  'logo')
