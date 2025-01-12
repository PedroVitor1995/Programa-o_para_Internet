"""myforms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.pagina_inicial, name='pagina_inicial'),
    path('listar_posts/', views.listar_posts, name='listar_posts'),
    path('adicionar_post/', views.adicionar_post, name='adicionar_post'),
    path('listar_artigos/', views.listar_artigos, name='listar_artigos'),
    path('adicionar_artigo/', views.adicionar_artigo, name='adicionar_artigo'),
    path('listar_livros/', views.listar_livros, name='listar_livros'),
    path('adicionar_livro/', views.adicionar_livro, name='adicionar_livro'),
]
