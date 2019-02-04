# serializers.py

from rest_framework import serializers
from .models import phoneContact, Snippets, LANGUAGE_CHOICES, STYLE_CHOICES

#Define serializers
class phoneContactSerializer(serializers.ModelSerializer):
	class Meta:
		model = phoneContact
		fields = ('id', 'first_name', 'last_name', 'phone_number', 'email', 'date_created', 'date_modified')
		read_only_fields = ('date_created', 'date_modified')

class SnippetsSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)
	title = serializers.CharField(required=True, allow_blank=True, max_length=100)
	code = serializers.CharField(style={'base_template': 'textarea.html'})
	linenos = serializers.BooleanField(required=False)
	language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
	style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

	def create(self, **validated_data):
		return Snippets.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.title = validated_data.get('title', instance.title)
		instance.code = validated_data.get('code', instance.code)
		instance.linenos = validated_data.get('linenos', instance.linenos)
		instance.language = validated_data.get('language', instance.language)
		instance.style = validated_data.get('style', instance.style)
		instance.save()
		return instance

	class Meta:
		model = Snippets
		exclude = []