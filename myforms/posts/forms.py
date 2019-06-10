from django.forms import ModelForm
from .models import Post,Reporter,Article,Autor,Book

class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ['titulo','texto']

class ReporterForm(ModelForm):
	class Meta:
		model = Reporter
		fields = ['nome']

class ArticleForm(ModelForm):
	class Meta:
		model = Article
		fields = '__all__'

class AutorForm(ModelForm):
	class Meta:
		model = Autor
		fields = '__all__'

class BookForm(ModelForm):
	class Meta:
		model = Book
		fields = '__all__'
