from django.db.models import fields
from rest_framework import serializers
from library.models import Job, AppList

# Second import



# First serializer

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Job
        fields = ['id', 'title', 'company', 'description', 'type', 'experience', 'profession']

# Second class for serializer
class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppList
        fields = ['id', 'name', 'email', 'birth_date', 'qualification',]