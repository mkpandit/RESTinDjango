#views.py

from django.shortcuts import render
from rest_framework import generics
from .serializers import phoneContactSerializer, SnippetsSerializer
from .models import phoneContact, Snippets

#View method for listing for GET (all) and POST
class CreateContactView(generics.ListCreateAPIView):
	queryset = phoneContact.objects.all()
	serializer_class = phoneContactSerializer

	def perform_create(self, serializer):
		serializer.save()

#view method for PUT, DELETE and GET (one)		
class DetailsContactView(generics.RetrieveUpdateDestroyAPIView):
	queryset = phoneContact.objects.all()
	serializer_class = phoneContactSerializer

#View method for listing for GET (all) and POST
class CreateSnippetsView(generics.ListCreateAPIView):
	queryset = Snippets.objects.all()
	serializer_class = SnippetsSerializer

	def perform_create(self, serializer):
		serializer.save()

#view method for PUT, DELETE and GET (one)		
class DetailsSnippetsView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Snippets.objects.all()
	serializer_class = SnippetsSerializer