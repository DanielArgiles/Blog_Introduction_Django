from django.db import models

class Post(models.Model):
# Create your models here.
	"""
	title= models.CharField(max_length=200)
	content= models.TextField()
	"""

	#En español: 
	title= models.CharField(max_length=200, verbose_name="Título")
	content= models.TextField(verbose_name="Contenido")
	
	#Veremos "Entrada" en lugar de "Post":
	class Meta:
		verbose_name="Entrada"
		verbose_name_plural="Entradas"
	
	#Veremos "Mi primera entrada" (que es el nombre de title) en lugar de "Post object(1) que es representacion en forma de cadena de un objeto por defecto en python:
	def __str__(self):
		return self.title
	