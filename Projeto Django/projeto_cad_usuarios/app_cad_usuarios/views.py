from django.shortcuts import render
from .models import Usuarios

# Create your views here.
def home(request):
   return render(request, 'usuarios/home.html') 

def usuarios(request):
   # Salvar os dados da tela para o Banco de Dados
   novo_usuario = Usuarios()
   novo_usuario.nome  = request.POST.get('nome')
   novo_usuario.idade = request.POST.get('idade')
   novo_usuario.save()
   # Exibir todos os usuários cadastrados em uma nova página
   usuarios = {
      'usuarios': Usuarios.objects.all()
   }
   
   # Retornar os dados para a página de listagem de usuários
   return render(request, 'usuarios/usuarios.html', usuarios)

   



