from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User


class PostsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ("title", "author", "description")

	def update(self, instance, validated_data):
		instance.title = validated_data.get("title", instance.title)
		instance.author = validated_data.get("author", instance.author)
		instance.description = validated_data.get("description", instance.description)
		instance.save()
		return instance


		# this serializer serializes the token data
class TokenSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'password', 'email')
		token = serializers.CharField(
		max_length = 255)

class LoginSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'password')