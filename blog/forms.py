from django import forms
from .models import Publication

TYPE_CHOISE = (
    ('Duvidas', 'Duvidas'),
    ('Erros', 'Erros'),
    ('Informações', 'Informações'),
    ('Outros', 'Outros'),
)

class PublicationForm (forms.ModelForm):
	class Meta:
		model = Publication
		fields = ('title', 'published_type', 'contet',)

	published_type = forms.ChoiceField(choices = TYPE_CHOISE)