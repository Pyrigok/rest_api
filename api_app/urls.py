from django.urls import path
from .views import ListPostsView, LoginView, RegisterUsersView
#  ListCreateBooksView, BooksDetailView,

urlpatterns = [
	path('auth/register/', RegisterUsersView.as_view(), name='auth-register'),
	path('auth/login/', LoginView.as_view(), name="auth-login"),
	path('posts/', ListPostsView.as_view(), name='posts_url'),
]