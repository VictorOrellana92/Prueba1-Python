from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse, reverse_lazy
from .models import Mascota

# Create your views here.

class MostrarMascota(ListView):
	model = Mascota
	template_name = "index.html"

mostrar_mascota = MostrarMascota.as_view()

class ListarMascota(CreateView):
	model = Mascota
	template_name = "crearMascota.html"
	fields = "__all__"
	success_url = reverse_lazy("mostrar_mascota")

listar_mascota = ListarMascota.as_view()