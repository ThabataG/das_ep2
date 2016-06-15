from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Publication
from .forms import PublicationForm

def publication_list(request):
	publication = Publication.objects.order_by('published_date')
	return render(request, 'blog/publication_list.html', {'publication':publication})

def publication_detail (request, pk):
	publication = get_object_or_404(Publication, pk=pk)
	return render(request, 'blog/publication_detail.html', {'publication': publication})

def publication_new(request):
	if request.method == "POST":
		form = PublicationForm(request.POST)
		if form.is_valid():
			publication = form.save (commit = False)
			publication.author = request.user
			publication.published_date = timezone.now()
			publication.save()
			return redirect ('blog.views.publication_detail', pk=publication.pk)
	else:
		form = PublicationForm()
	return render (request, 'blog/publication_edit.html', {'form':form})

def publication_edit(request, pk):
	publication = get_object_or_404(Publication, pk=pk)
	if request.method == "POST":
		form = PublicationForm(request.POST, instance = publication)
		if form.is_valid():
			publication = form.save (commit = False)
			publication.author = request.user
			publication.published_date = timezone.now()
			publication.save()
			return redirect ('blog.views.publication_detail', pk=publication.pk)
	else:
		form = PublicationForm(instance = publication)
	return render (request, 'blog/publication_edit.html', {'form': form})