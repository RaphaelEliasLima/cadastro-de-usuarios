
from django.urls import path
from app_cadastro_usuarios import views

urlpatterns = [
    #rota, view responsavel, nome de referencia
    #usuarios.com
    path('', views.home,name='home'),
    #usuarios.com/usuarios
    path("usuarios/",views.usuarios,name="listagem_usuarios")
    ]
