from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

# Função para exibir o perfil do usuário
def profile(request):
    if request.user.is_authenticated:
        # Renderiza a página de perfil se o usuário estiver autenticado
        return render(request, "registration/profile.html")
    else:
        # Redireciona para a página de login caso o usuário não esteja autenticado
        return HttpResponseRedirect(reverse('login'))

# Função para cadastro de novos usuários
def signup(request):
    if request.method == 'POST':  # Verifica se o método da requisição é POST
        username = request.POST['username']  # Obtém o nome de usuário do formulário
        email = request.POST['mail']         # Obtém o email do formulário
        password = request.POST['pass1']     # Obtém a senha do formulário
        nameerror = None
        emailerror = None

        # Verifica se o nome de usuário já existe
        if username in User.objects.values_list('username', flat=True):
            nameerror = "O nome de usuário já existe"

        # Verifica se o email já está em uso
        if email in User.objects.values_list('email', flat=True):
            emailerror = "Este email já está em uso"

        # Caso não haja erros, cria o usuário e faz login
        if not nameerror and not emailerror:
            user = User.objects.create_user(username, email, password)
            login(request, user)  # Faz login do novo usuário
            return HttpResponseRedirect(reverse('home'))  # Redireciona para a página inicial

        else:
            # Renderiza novamente a página de cadastro com mensagens de erro
            return render(request, "registration/signup.html", context={
                'nameerror': nameerror,
                'emailerror': emailerror,
            })
    else:
        # Renderiza a página de cadastro para métodos que não sejam POST
        return render(request, "registration/signup.html")
