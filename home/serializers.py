from rest_framework import serializers
from . import models


class PersonSerializer(serializers.ModelSerializer):
    car = serializers.StringRelatedField()
    class Meta:
        model = models.Person
        fields = ['id', 'name', 'age', 'car']
        extra_kwargs = {
            'email': {'write_only': True},
            'name': {'help_text': 'Select character and number and _ !@#'}
        }