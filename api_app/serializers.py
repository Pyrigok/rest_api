from rest_framework import serializers
from .models import Books_Model

class BooksSerializer(serializers.ModelSerializer):
	class Meta:
		model = Books_Model
		fields = ("title", "author", "description")
		