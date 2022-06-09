
from django.urls import path
from AppCoder import views

urlpatterns = [
    path("medicos/", views.medicos, name="medicos"),
    path("inicio/", views.inicio, name="inicio"),
    path("pacientes/", views.pacientes, name="pacientes"),
    path("clinicas/", views.clinicas, name="clinicas"),
    path("contactoFormulario/", views.contactoFormulario, name="contactoFormulario"),
    path("busquedaProfesional/", views.busquedaProfesional, name="busquedaProfesional"),
    path("buscar/", views.buscar, name="buscar")
]
