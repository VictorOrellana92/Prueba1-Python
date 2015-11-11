from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.mostrar_mascota, name = 'mostrar_mascota'),
	url(r'^nuevaMascota/$', views.listar_mascota, name = 'nueva_mascota'),
]