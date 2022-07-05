
from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("medicos/", views.leerMedicos, name="medicos"),
    path("aboutme/",views.aboutMe, name="aboutMe"),
    path("inicio/", views.inicio, name="inicio"),
    path("pacientes/", views.pacientes, name="pacientes"),
    path("clinicas/", views.clinicas, name="clinicas"),
    path("contactoFormulario/", views.contactoFormulario, name="contactoFormulario"),
    path("busquedaProfesional/", views.busquedaProfesional, name="busquedaProfesional"),
    path("buscar/", views.buscar, name="buscar"),
    path("eliminarMedico/<nombre>", views.eliminarMedico, name="eliminarMedico"),
    path("editarMedico/<medico_nombre>", views.editarMedico, name="editarMedico"),
    path("pages/", views.PacientesList.as_view(), name="paciente_listar"),
    path("pages/<pk>", views.PacienteDetalle.as_view(), name="paciente_detalle"),
    path("paciente/nuevo/", views.PacienteCreacion.as_view(), name="paciente_crear"),
    path("paciente/editar/<pk>", views.PacienteEdicion.as_view(), name="paciente_editar"),
    path("paciente/borrar/<pk>", views.PacienteEliminacion.as_view(), name="paciente_borrar"),
    path("accounts/login", views.login_request, name="login"),
    path("accounts/signup", views.register_request, name="register"),
    path("logout", LogoutView.as_view(template_name='appCoder/logout.html'), name="logout"),
    path("accounts/profile", views.editarPerfil, name="editarPerfil"),
]

