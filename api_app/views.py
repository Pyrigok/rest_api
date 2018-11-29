from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework.views import APIView

#from django.http import HttpResponse, JsonResponse
#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser


from rest_framework_jwt.settings import api_settings

from .models import PostModel
from .serializers import PostsSerializer, TokenSerializer, LoginSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated



class ListPostsView(generics.ListCreateAPIView):
	"""Provides a get method handler"""

	queryset = PostModel.objects.all()
	serializer_class = PostsSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = PostModel.objects.all()
	serializer_class = PostsSerializer
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
#	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


# get the JWT settins
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


	#	POST auth/login/
	# this class override the global permission class setting
class LoginView(generics.CreateAPIView):

	permission_classes = (permissions.AllowAny,)
	queryset = User.objects.all()
	serializer_class = LoginSerializer


	def post(self, request, *args, **kwargs):

		username = request.data.get("username", "")
		password = request.data.get("password", "")
		user = authenticate(request, username=username, password=password)

		if user is not None:

			# login saves user's ID in the session using Django's session framework
			login(request, user)
			serializer = TokenSerializer(data={
				# using drf jwt utility functions to generate a token
				"token": jwt_encode_handler(
					jwt_payload_handler(user)
				)})
			serializer.is_valid()

			return Response(
				#serializer.data,
				data={
				"message": "User %s entered successful!" %username
				}
				)
		return Response(status=status.HTTP_401_UNAUTHORIZED)


		# User Register
class RegisterUsersView(generics.CreateAPIView):

	permission_classes = (permissions.AllowAny,)
	serializer_class = TokenSerializer

	def post(self, request, *args, **kwargs):
		username = request.data.get("username", "")
		password = request.data.get("password", "")
		email = request.data.get("email", "")
		
		if not username and not password and not email:
			return Respomse(
				data={
				"message": "username, password and email is required to register a user!"
				},
				status = status.HTTP_400_BAD_REQUEST
			)

		new_user = User.objects.create_user(
			username=username, password=password, email=email
		)

		return Response(
			data={
				"message": "Registration was succesful!"
				},
			status=status.HTTP_201_CREATED)

class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer