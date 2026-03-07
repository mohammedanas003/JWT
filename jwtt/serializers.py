from rest_framework.serializers import ModelSerializer
from .models import Teacher

class Teacher_serializers(ModelSerializer):
    class Meta:
        model=Teacher
        fields="__all__"