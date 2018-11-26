from django.test import TestCase, Client
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from django.urls import reverse
from .models import Post
from .serializers import PostsSerializer

# test for views
class TestView(TestCase):
	client = APIClient()

	@staticmethod
	def test_create_post(title="", author="", description=""):
		if title != "" and author != "":
			Post.objects.create(title=title, author=author, description=description)

	def setUp(self):
		# add test data
		self.test_create_post("post 1", "author1_first_name author1_last_name", "book_1 description")
		self.test_create_post("post 2", "author2_first_name author2_last_name", "book_2 description")
		self.test_create_post("post 3", "author3_first_name author3_last_name")

	#This test ensures that all books added in the setUp method exist when we make
	#a GET request to the books/endpoint
class TestGetAllPosts(TestView):

	def test_get_all_posts(self):
		response = self.client.get(reverse("posts_url", kwargs={"version": "v1"}))
		expected = Post.objects.all()
		serialized = PostsSerializer(expected, many = True)
		self.assertEqual(response.data, serialized.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
