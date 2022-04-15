from rest_framework import serializers
from .models import Resume


class ResumeSerializer(serializers.ModelSerializer):
    """
    Serializing all the Resumes
    """

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Resume
        fields = ('id', 'name', 'surname', 'status', 'salary', 'grade',
                  'education', 'experience', 'specialty', 'user', 'portfolio')
