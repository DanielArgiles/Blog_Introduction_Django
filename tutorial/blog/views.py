from django.shortcuts import render,HttpResponse # render para renderizar plantillas html
from .models import Post

# Create your views here.


"""
def home (request): # Esta función se encarga de la vista en http://127.0.0.1:8000/ en texto plano
	return HttpResponse("Bienvenido a mi blog")


"""
def home(request): # Renderizamos un template html home.html bien estructurado
	posts= Post.objects.all()
	return render (request, "blog/home.html",{'posts':posts}) # {} diccionario de contexto, clave 'posts' y el valor que devuelve es la lista posts recuperada de la base de datos

def post(request,id):
	post= Post.objects.get(id=id)
	return render(request,"blog/post.html",{'post':post})