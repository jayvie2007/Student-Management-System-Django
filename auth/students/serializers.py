from .models import Student
from rest_framework import serializers

class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'