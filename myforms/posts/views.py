from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Post

# Create your views here.

def pagina_principal(request):
	posts = Post.objects.all()
	return render(request,'pagina_principal.html',{'posts':posts})

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

