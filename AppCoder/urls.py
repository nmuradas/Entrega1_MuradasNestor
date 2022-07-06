
from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("autores/", views.leerAutores, name="autores"),
    path("aboutme/",views.aboutMe, name="aboutMe"),
    path("inicio/", views.inicio, name="inicio"),
    path("contactoFormulario/", views.contactoFormulario, name="contactoFormulario"),
    path("eliminarAutor/<nombre>", views.eliminarAutor, name="eliminarAutor"),
    path("editarAutor/<autor_nombre>", views.editarAutor, name="editarAutor"),
    path("pages/", views.BlogsList.as_view(), name="blog_listar"),
    path("pages/<pk>", views.BlogDetalle.as_view(), name="blog_detalle"),
    path("autor/nuevo/", views.AutorCreacion.as_view(), name="autor_crear"),
    path("blog/nuevo/", views.BlogCreacion.as_view(), name="blog_crear"),
    path("blog/editar/<pk>", views.BlogEdicion.as_view(), name="blog_editar"),
    path("blog/borrar/<pk>", views.BlogEliminacion.as_view(), name="blog_borrar"),
    path("accounts/login", views.login_request, name="login"),
    path("accounts/signup", views.register_request, name="register"),
    path("logout", LogoutView.as_view(template_name='appCoder/logout.html'), name="logout"),
    path("accounts/profile", views.editarPerfil, name="editarPerfil"),
]

