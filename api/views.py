#views.py

from django.shortcuts import render
from rest_framework import generics
from .serializers import phoneContactSerializer
from .models import phoneContact

#View method for listing for GET (all) and POST
class CreateView(generics.ListCreateAPIView):
	queryset = phoneContact.objects.all()
	serializer_class = phoneContactSerializer

	def perform_create(self, serializer):
		serializer.save()

#view method for PUT, DELETE and GET (one)		
class DetailsView(generics.RetrieveUpdateDestroyAPIView):
	queryset = phoneContact.objects.all()
	serializer_class = phoneContactSerializer