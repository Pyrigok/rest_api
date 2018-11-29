from rest_framework import serializers
from .models import PostModel
from django.contrib.auth.models import User


class PostsSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	title = serializers.CharField(required=True, allow_blank=False, max_length=50)
	author = serializers.CharField(required=True, allow_blank=False, max_length=100)
	description = serializers.CharField(required=True, allow_blank=False, max_length=100)
	owner = serializers.ReadOnlyField(source='owner.username')
	votes = serializers.BooleanField(required=False)

	def create(self, validated_data):
		return PostModel.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.title = validated_data.get('title', instance.title)
		instance.author = validated_data.get('author', instance.author)
		instance.description = validated_data.get('description', instance.description)
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



class UserSerializer(serializers.ModelSerializer):
	posts = serializers.PrimaryKeyRelatedField(many=True, queryset=PostModel.objects.all())

	class Meta:
		model = User
		fields = ('id', 'username')
