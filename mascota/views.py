from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views import generic
from django.core.urlresolvers import reverse, reverse_lazy
from .models import Mascota, Mascota_Perdida, Mascota_Encontrada

# Create your views here.

class MostrarMascota(ListView):
	model = Mascota
	template_name = "index.html"

	def get_context_data(self, **kwargs):
	    # Call the base implementation first to get a context
	    cursor = super(MostrarMascota, self).get_context_data(**kwargs)

	    # Add in a QuerySet of all the books
	    cursor['mascotas_encontradas'] = Mascota_Encontrada.objects.filter(lugar_encuentro = "Maipu", lugar_extravio = "0")
	    #Book.objects.filter(publisher__name="Acme Publishing")
	    return cursor

mostrar_mascota = MostrarMascota.as_view()


class ListarMascota(CreateView):
	model = Mascota
	template_name = "crearMascota.html"
	fields = "__all__"
	success_url = reverse_lazy("mostrar_mascota")

listar_mascota = ListarMascota.as_view()

def mascotaPerdida(request):
	perdidos = Mascota_Perdida.objects.all()
	return render_to_response('mascotaPerdida.html',{'perdidos': perdidos})

