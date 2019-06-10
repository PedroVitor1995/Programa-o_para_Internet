from django.shortcuts import render,redirect
from .forms import PostForm,ArticleForm,BookForm
from .models import Post,Article,Book

# Create your views here.

def pagina_inicial(request):
	posts = Post.objects.all()
	artigos = Article.objects.all()
	livros = Book.objects.all()
	return render(request,'pagina_inicial.html',{'posts':posts,'artigos':artigos,'livros':livros})

def listar_posts(request):
	posts = Post.objects.all()
	return render(request,'listar_posts.html',{'posts':posts})

def adicionar_post(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			model_instance = form.save(commit=False)
			model_instance.save()
			return redirect('listar_posts')
	else:
		form = PostForm()
		return render(request,'adicionar_post.html',{'form':form})

def listar_artigos(request):
	artigos = Article.objects.all()
	return render(request,'listar_artigos.html',{'artigos':artigos})

def adicionar_artigo(request):
	if request.method == 'POST':
		form = ArticleForm(request.POST)
		if form.is_valid():
			model_instance = form.save(commit=False)
			model_instance.save()
			return redirect('listar_artigos')
	else:
		form = ArticleForm()
		return render(request,'adicionar_artigo.html',{'form':form})

def listar_livros(request):
	livros = Book.objects.all()
	return render(request,'listar_livros.html',{'livros':livros})

def adicionar_livro(request):
	if request.method == 'POST':
		form = BookForm(request.POST)
		if form.is_valid():
			model_instance = form.save(commit=False)
			model_instance.save()
			return redirect('listar_livros')
	else:
		form = BookForm()
		return render(request,'adicionar_livro.html',{'form':form})
