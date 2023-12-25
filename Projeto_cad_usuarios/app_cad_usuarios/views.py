from django.shortcuts import render
from .models import usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    novo_usuario = usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    #Exibir todos os usuarios em uma nova pagina
    usuarios ={
        'usuarios': usuario.objects.all()
    }

    #retornar os dados para pagina de usuarios
    return render(request, 'usuarios/usuarios.html', usuarios)
