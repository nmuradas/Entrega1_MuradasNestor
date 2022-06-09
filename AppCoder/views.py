from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Medico, Paciente, Clinica  #traigo la tabla
from django.template import loader  
from AppCoder.forms import ContactoFormulario
# Create your views here.

def inicio(self):
    plantilla = loader.get_template('appCoder/inicio.html')
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
        edad= informacion['edad']
        contacto = Paciente(nombre = nombre, apellido = apellido, email = email, edad=edad)
        contacto.save()
        return render(request, 'appCoder/inicio.html')
    else:
        miFormulario = ContactoFormulario()
    return render(request, 'appCoder/contactoFormulario.html', {'miFormulario':miFormulario})

def busquedaProfesional(request):
    return render(request, 'appCoder/busquedaProfesional.html')

def buscar(request):
    if request.GET['especialidad']:
        especialidad = request.GET['especialidad']
        medicos = Medico.objects.filter(especialidad=especialidad)
        return render(request, 'appCoder/resultadosBusqueda.html', {'medicos':medicos, 'especialidad': especialidad})
    else:
        respuesta = "No se ha encontrado ningún profesional"
    return HttpResponse(respuesta)