from django.urls import path
from usuarios import views
from usuarios.views import RegistrarUsuarioView
from django.contrib.auth import views as v

urlpatterns = [
    path('registrar/', RegistrarUsuarioView.as_view(),name="registrar"),
    path('login/',v.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',v.LogoutView.as_view(template_name='login.html'),name='logout'),
]