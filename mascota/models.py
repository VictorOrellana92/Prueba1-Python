from django.db import models

# Create your models here.


class Usuario(models.Model):

    nombre = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    comuna = models.CharField(max_length = 30)   
   
    def __unicode__(self):
        return self.nombre

class Mascota(models.Model):
	id_usuario = models.ForeignKey('Usuario')
	nombre = models.TextField()
	sexo = models.CharField(max_length=10)
	fecha_nacimiento = models.DateField('')
	color = models.TextField()
	comuna_residencia = models.TextField()
	comentario = models.TextField()
	raza = models.TextField()
	foto = models.TextField()

	def __unicode__(self):
		return self.nombre

class Mascota_Perdida(models.Model):
	id_mascota = models.ForeignKey('Mascota')
	nombre = models.CharField(max_length=20)
	fecha_extravio = models.DateField('')
	lugar_extravio = models.CharField(max_length = 100)
	recompensa = models.TextField()
	foto =  models.TextField()

	def __unicode__(self):
		return self.nombre

class Caza_Recompensas(models.Model):
	id_usuario = models.ForeignKey('Usuario')
	def __unicode__(self):
		return self.id_usuario

class Mascota_Encontrada(models.Model):
	id_caza_recompensa = models.ForeignKey('Caza_Recompensas')
	fecha_encuentro = models.DateField('')
	lugar_encuentro = models.CharField(max_length = 100)
	comentario = models.TextField()
	sexo = models.TextField()
	razaa = models.TextField()
	foto =  models.TextField()

	def __unicode__(self):
		return self.nombre