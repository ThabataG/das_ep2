from django.contrib import admin
from .models import Publication

class BlogAdmin(admin.ModelAdmin):
	list_display = ['author', 'title', 'published_date']
	list_filter = ['author', 'title', 'published_date']
	search_fields = ['title']
	save_on_top = True
	
admin.site.register (Publication, BlogAdmin)