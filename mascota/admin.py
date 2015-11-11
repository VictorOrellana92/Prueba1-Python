from django.contrib import admin
from .models import Usuario,Mascota,Mascota_Perdida,Caza_Recompensas,Mascota_Encontrada

# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
	list_display = ['nombre', 'phone', 'email', 'comuna']

@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
	list_display = ['id_usuario', 'nombre', 'sexo', 'fecha_nacimiento', 'color', 'comuna_residencia', 'comentario', 'raza']

@admin.register(Mascota_Perdida)
class Mascota_PerdidaAdmin(admin.ModelAdmin):
	list_display = ['id_mascota', 'nombre', 'fecha_extravio', 'lugar_extravio', 'recompensa']

@admin.register(Caza_Recompensas)
class Caza_RecompensasAdmin(admin.ModelAdmin):
	list_display = ['id_usuario']

@admin.register(Mascota_Encontrada)
class Mascota_EncontradaAdmin(admin.ModelAdmin):
	list_display = ['id_caza_recompensa', 'fecha_encuentro', 'lugar_encuentro', 'comentario', 'sexo', 'razaa']