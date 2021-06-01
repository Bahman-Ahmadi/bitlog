from django.contrib import admin
from blog.models import *

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'pubTime', 'status')
	list_filter = ('pubTime', 'status')
	search_fields = ('title', 'note')
	prepopulated_fields = {'slug': ('title',)}
	ordering = ['-status', '-pubTime']

# Register your models here.
admin.site.register(Post, PostAdmin)