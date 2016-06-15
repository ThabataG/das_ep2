from django.shortcuts import render
from django.utils import timezone
from .models import Publication

def publication_list(request):
	publication = Publication.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/publication_list.html', {'publication':publication})
