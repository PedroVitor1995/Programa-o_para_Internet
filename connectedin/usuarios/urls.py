from django.urls import path
from usuarios import views
from usuarios.views import RegistrarUsuarioView
from django.contrib.auth import views as v

urlpatterns = [
    path('registrar/', RegistrarUsuarioView.as_view(),name="registrar"),
    path('login/',v.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',v.LogoutView.as_view(template_name='login.html'),name='logout'),
    path('redefinir_senha/',v.PasswordResetView.as_view(template_name='redefinir_senha.html'),\
    	name='redefinir_senha'),
    path('redefinir_senha/done/',v.PasswordResetDoneView.as_view(template_name='redefinir_senha_done.html'),\
    	name='redefinir_senha_done'),
    path('reset/<uidb64>/<token>/',v.PasswordResetConfirmView.as_view(template_name='redefinir_senha_confirm.html'),\
    name='password_reset_confirm'),
    path('reset/done',v.PasswordResetCompleteView.as_view(template_name='redefinir_senha_complete.html'),\
    name='redefinir_senha_complete'),
]


