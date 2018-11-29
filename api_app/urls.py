from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ListPostsView, PostDetailView, LoginView, RegisterUsersView, UserList

#from votes import urls

urlpatterns = [

	path('auth/register/', RegisterUsersView.as_view(), name='auth_register_url'),
	path('auth/login/', LoginView.as_view(), name="auth_login_url"),
	path('users/', UserList.as_view(), name="users_list_url"),
	
	path('', ListPostsView.as_view(), name='posts_url'),
	path('details/<int:pk>', PostDetailView.as_view(), name='posts_detail_url'),

	#path('votes/', include(urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)

