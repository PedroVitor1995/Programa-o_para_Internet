<<<<<<< HEAD
from django.forms import ModelForm
from perfis.models import Postagem

class PostagemForm(ModelForm):
	class Meta:
		model = Postagem
		fields = '__all__'
=======
from django import forms

class PostForm(forms.Form):
	texto_postagem = forms.CharField(required=True)
	imagem_postagem = forms.FileField(required=False)
>>>>>>> eb8ab2b85d20b1d5fa04c7258dfb7922f5545dd1
