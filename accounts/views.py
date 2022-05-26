from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as log, logout as logt
from accounts.forms import FormCadastro

def cadastro(request):
    if not request.user.is_authenticated:
        if request.method == 'GET':
            form = FormCadastro()
            return render(request, 'accounts/cadastro.html', {'form': form})
        else:
            form = FormCadastro(request.POST or None)
            if form.is_valid():
                user = form.save(commit=False)
                new_user = User.objects.create_user(username=user.username,
                first_name=user.first_name, last_name=user.last_name,
                email=user.email, password=user.password, is_active=True,
                is_staff=False, is_superuser=True)
                new_user.save()
                return redirect('login')
            else:
                return render(request, "accounts/cadastro.html", {'form': form})
    else:
        return redirect ('agenda/')
def login(request):
    if not request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'accounts/login.html')
        else:
            usuario = request.POST['usuario']
            senha = request.POST['senha']
            user = authenticate(request, username=usuario, password=senha)
            if user is not None:
                log(request, user)
                return redirect('agenda/')
            else:
                return redirect('login')
    else:
        return redirect ('agenda/')

def logout(request):
    logt(request)
    return redirect('login')