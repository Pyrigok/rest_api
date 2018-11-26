from django.shortcuts import render
from rest_framework import generics
from .models import Books_Model
from .serializers import BooksSerializer

class ListBooksView(generics.ListAPIView):
	"""Provides s get method handler"""

	queryset = Books_Model.objects.all()
	serializer_class = BooksSerializer