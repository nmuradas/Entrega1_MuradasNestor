from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Autor, Blog, Invitados  #traigo la tabla
from django.template import loader  
from AppCoder.forms import ContactoFormulario, AutorFormulario,  UserResgistrationForm, UserEditForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

def inicio(self):
    plantilla = loader.get_template('appCoder/inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def aboutMe(self):
    plantilla = loader.get_template('appCoder/aboutme.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def autores(request):
    return render(request, 'appCoder/autores.html')


def contactoFormulario(request):
    if request.method == 'POST':
        miFormulario = ContactoFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombre= informacion['nombre']
        apellido= informacion['apellido']
        email= informacion['email']
        contacto = Invitados(nombre = nombre, apellido = apellido, email = email)
        contacto.save()
        return render(request, 'appCoder/inicio.html')
    else:
        miFormulario = ContactoFormulario()
    return render(request, 'appCoder/contactoFormulario.html', {'miFormulario':miFormulario})

def leerAutores(request):
    autores = Autor.objects.all()
    contexto = {'autores':autores} 
    return render(request, 'appCoder/autores.html', contexto )

@login_required
def eliminarAutor(request, nombre):
    autor = Autor.objects.get(nombre=nombre)
    autor.delete()
    autores = Autor.objects.all()
    contexto = {'autores':autores} 
    return render(request, 'appCoder/autores.html', contexto)

@login_required
def editarAutor(request, autor_nombre):
    autor = Autor.objects.get(nombre=autor_nombre) 
    if request.method == 'POST':
        miFormulario = AutorFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            autor.nombre= informacion['nombre']
            autor.apellido = informacion['apellido']
            autor.email = informacion['email']
            autor.profesion = informacion['profesion']
            autor.save()

            autores = Autor.objects.all()     
            contexto = {'autores':autores}
            return render(request, 'appCoder/autores.html', contexto )
    else:
        miFormulario = AutorFormulario(initial={'nombre':autor.nombre, 'apellido':autor.apellido, 'email':autor.email, 'profesion':autor.profesion})
        contexto = {'miFormulario': miFormulario, 'autor_nombre': autor_nombre}
        return render(request, 'appCoder/editarAutor.html', contexto )


class BlogsList(ListView): 
    model = Blog
    template_name = 'appCoder/blog_list.html'


class BlogDetalle(DetailView): 
    model = Blog
    template_name = 'appCoder/blog_detalle.html'


class BlogCreacion(LoginRequiredMixin, CreateView): 
    model = Blog
    success_url = reverse_lazy('blog_listar')
    fields = ['titulo','subtitulo', 'cuerpo', 'autor','fecha', 'imagen']


class BlogEdicion(LoginRequiredMixin, UpdateView): 
    model = Blog
    success_url = reverse_lazy('blog_listar')
    fields = ['titulo','subtitulo', 'cuerpo', 'autor','fecha', 'imagen']

class BlogEliminacion(LoginRequiredMixin, DeleteView): 
    model = Blog
    success_url = reverse_lazy('blog_listar')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'appCoder/inicio.html', {'mensaje': f'Bienvenido {username}'})
            else:
                return render(request, 'appCoder/inicio.html', {'mensaje': 'Datos incorrectos'})
        else:
            return render(request, 'appCoder/inicio.html', {'mensaje': 'Datos incorrectos'})
    
    form = AuthenticationForm()
    return render(request, 'appCoder/login.html', {'form': form})

def register_request(request):
    if request.method == 'POST':
        form =  UserResgistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'appCoder/inicio.html', {'mensaje': f'Usuario {username} creado'})
        else:
            return render(request, 'appCoder/inicio.html', {'mensaje': 'Error, no se pudo crear el usuario'})
    else:
        form = UserResgistrationForm()
        return render(request, 'appCoder/register.html', {'form': form})

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        formulario = UserEditForm(request.POST, instance=usuario)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()
            return render(request, 'appCoder/inicio.html', {'usuario':usuario, 'mensaje':'Datos cambiados exitosamente'})
    else:
        formulario = UserEditForm(instance=usuario)
    return render(request, 'appCoder/editarPerfil.html', {'usuario':usuario.username, 'formulario':formulario})