from django import forms

class PostForm(forms.Form):
	texto_postagem = forms.CharField(required=True)
	imagem_postagem = forms.FileField(required=False)