from django import forms
from django.forms import ModelForm
from perfis.models import *


class PostagemForm(ModelForm):
	class Meta:
		model = Postagem
		fields = '__all__'

