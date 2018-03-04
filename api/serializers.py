# serializers.py

from rest_framework import serializers
from .models import phoneContact

#Define serializers
class phoneContactSerializer(serializers.ModelSerializer):
	class Meta:
		model = phoneContact
		fields = ('id', 'first_name', 'last_name', 'phone_number', 'email', 'date_created', 'date_modified')
		read_only_fields = ('date_created', 'date_modified')