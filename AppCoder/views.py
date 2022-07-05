from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Medico, Paciente  #traigo la tabla
from django.template import loader  
from AppCoder.forms import ContactoFormulario, MedicoFormulario,  UserResgistrationForm, UserEditForm
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

def medicos(request):
    return render(request, 'appCoder/medicos.html')

def pacientes(request):
    return render(request, 'appCoder/pacientes.html')

def clinicas(request):
    return render(request, 'appCoder/clinicas.html')


def contactoFormulario(request):
    if request.method == 'POST':
        miFormulario = ContactoFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombre= informacion['nombre']
        apellido= informacion['apellido']
        email= informacion['email']
        contacto = Paciente(nombre = nombre, apellido = apellido, email = email)
        contacto.save()
        return render(request, 'appCoder/inicio.html')
    else:
        miFormulario = ContactoFormulario()
    return render(request, 'appCoder/contactoFormulario.html', {'miFormulario':miFormulario})

def busquedaProfesional(request):
    return render(request, 'appCoder/busquedaProfesional.html')

def buscar(request):
    if request.GET['profesion']:
        profesion = request.GET['profesion']
        medicos = Medico.objects.filter(profesion=profesion)
        return render(request, 'appCoder/resultadosBusqueda.html', {'medicos':medicos, 'profesion': profesion})
    else:
        respuesta = "No se ha encontrado ningún profesional"
    return HttpResponse(respuesta)

def leerMedicos(request):
    medicos = Medico.objects.all()
    contexto = {'medicos':medicos} 
    return render(request, 'appCoder/medicos.html', contexto )

@login_required
def eliminarMedico(request, nombre):
    medico = Medico.objects.get(nombre=nombre)
    medico.delete()
    medicos = Medico.objects.all()
    contexto = {'medicos':medicos} 
    return render(request, 'appCoder/medicos.html', contexto)

@login_required
def editarMedico(request, medico_nombre):
    medico = Medico.objects.get(nombre=medico_nombre) 
    if request.method == 'POST':
        miFormulario = MedicoFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            medico.nombre= informacion['nombre']
            medico.apellido = informacion['apellido']
            medico.email = informacion['email']
            medico.profesion = informacion['profesion']
            medico.save()

            medicos = Medico.objects.all()     
            contexto = {'medicos':medicos}
            return render(request, 'appCoder/medicos.html', contexto )
    else:
        miFormulario = MedicoFormulario(initial={'nombre':medico.nombre, 'apellido':medico.apellido, 'email':medico.email, 'profesion':medico.profesion})
        contexto = {'miFormulario': miFormulario, 'medico_nombre': medico_nombre}
        return render(request, 'appCoder/editarMedico.html', contexto )

class PacientesList(LoginRequiredMixin, ListView): #lee todos los estudiantes
    model = Paciente
    template_name = 'appCoder/paciente_list.html'

class PacienteDetalle(DetailView): #lee uno en particular
    model = Paciente
    template_name = 'appCoder/paciente_detalle.html'

class PacienteCreacion(CreateView): #crea una vista 
    model = Paciente
    success_url = reverse_lazy('paciente_listar')
    fields = ['nombre','apellido', 'email']


class PacienteEdicion(UpdateView): #actualiza una vista 
    model = Paciente
    success_url = reverse_lazy('paciente_listar')
    fields = ['nombre','apellido', 'email']

class PacienteEliminacion(DeleteView): #elimina el objeto completo una vista 
    model = Paciente
    success_url = reverse_lazy('paciente_listar')

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