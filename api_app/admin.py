from django.contrib import admin
from .models import PostModel

class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'author', 'owner']
	ordering = ['title', 'author', 'owner']

admin.site.register(PostModel, PostAdmin)
