from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    if request.method == 'POST':
        # Salvar o novo usuário no banco de dados
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get("nome")
        novo_usuario.idade = request.POST.get("idade")
        novo_usuario.email = request.POST.get("Email")
        novo_usuario.save()

    # Exibir todos os usuários já cadastrados
    usuarios_cadastrados = Usuario.objects.all()

    # Configurar o contexto para renderizar o template
    contexto = {
        'usuarios': usuarios_cadastrados
    }

    # Retornar os dados para a página
    return render(request, "usuarios/usuarios.html", contexto)
