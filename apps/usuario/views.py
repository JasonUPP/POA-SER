from django.shortcuts import render
from django.http import HttpResponse
from apps.usuario.forms import UsuarioForm
from apps.usuario.forms import RegistroForm
from apps.usuario.models import Usuario
from django.urls import path, include
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView
from django.views.generic import ListView
from django.shortcuts import redirect

class SignUp(generic.CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def user_list(request):
	user = User.objects.all().order_by('id')
	contexto = {'users':user}
	return render(request, 'usuario/user_list.html', contexto)

def user_edit(request, id_user):
	user = User.objects.get(id=id_user)
	if request.method == 'GET':
		form = RegistroForm(instance=user)
	else:
		form = RegistroForm(request.POST, instance=user)
		if form.is_valid():
			form.save()
		return redirect('list')
	return render(request, 'registration/signup.html', {'form':form})

def user_delete(request, id_user):
	user = User.objects.get(id=id_user)
	if request.method == 'POST':
		user.delete()
		return redirect('list')
	return render(request, 'registration/user_delete.html', {'user':user})

def index(request):
	return render(request, 'index.html')


#------------------------------ Primeras cosas ------------------
#usuario_view es para crear
def usuario_view(request):
	if request.method == "POST":
		form= UsuarioForm(request.POST)
		if form.is_valid():
			usuario = form.save()
			return redirect('index')
	else:
		form = UsuarioForm()
	return render(request, 'usuario/formulario.html', {'form':form})

def usuario_list(request):
	usuario = Usuario.objects.all().order_by('id')
	contexto = {'usuarios':usuario}
	return render(request, 'usuario/usuario_list.html', contexto)

def usuario_edit(request, id_usuario):
	usuario = Usuario.objects.get(id=id_usuario)
	if request.method == 'GET':
		form = UsuarioForm(instance=usuario)
	else:
		form = UsuarioForm(request.POST, instance=usuario)
		if form.is_valid():
			form.save()
		return redirect('listar')
	return render(request, 'usuario/formulario.html', {'form':form})

def usuario_delete(request, id_usuario):
	usuario = Usuario.objects.get(id=id_usuario)
	if request.method == 'POST':
		usuario.delete()
		return redirect('listar')
	return render(request, 'usuario/usuario_delete.html', {'usuario':usuario})
