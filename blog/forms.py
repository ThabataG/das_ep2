from django import forms
from .models import Publication, Contact
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

TYPE_CHOISE = (
    ('Duvidas', 'Duvidas'),
    ('Erros', 'Erros'),
    ('Informações', 'Informações'),
    ('Discussões', 'Discussões'),
    ('Outros', 'Outros'),
)

class PublicationForm (forms.ModelForm):
	class Meta:
		model = Publication
		fields = ('title', 'published_type', 'contet',)

	published_type = forms.ChoiceField(choices = TYPE_CHOISE)

class ContactForm(forms.Form):
	class Meta:
		model = Contact
		fields = ('subject', 'message', 'from_email',)