from django import forms
from perfis.models import *


class PostagemForm(forms.Form):
	class Meta:
		model = Postagem
		fields = '__all__'

