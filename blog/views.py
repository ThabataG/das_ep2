from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Publication
from .models import Contact
from .forms import PublicationForm
from .forms import ContactForm

def publication_list(request):
	publication = Publication.objects.order_by('-published_date')
	var_get_search = request.GET.get('search_box')
	if var_get_search is not None:
		publication = publication.filter(title__icontains=var_get_search)
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

@login_required(login_url='/accounts/login/')
def protected_view(request):
    return render(request, 'blog/protected.html', {'current_user': request.user})

def message(request):
    return HttpResponse('Accesso Negado!')

def form_contact(request):
	if request.method == "POST":
		form = ContactForm(request.POST)

		if form.is_valid():
		    subject = request.POST.get('subject', '')
		    message = request.POST.get('message', '')
		    from_email = request.POST.get('from_email', '')
		    if subject and message and from_email:
		        try:
		            send_mail(subject, message, from_email, ['admin@example.com'])
		        except BadHeaderError:
		            return HttpResponse('Invalid header found.')
		        return HttpResponseRedirect('/contact/thanks/')
		    else:
		        return HttpResponse('Make sure all fields are entered and valid.')
	else:
		form = ContactForm()
	return render (request, 'blog/email.html', {'form':form})