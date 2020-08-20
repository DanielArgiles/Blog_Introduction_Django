
"""
https://www.hektorprofe.net/curso/curso-django-principiantes/configuracion-django-basica
1- ¿QUÉ ES DJANGO?
Framework web backend
Programado en python
Gratuito y licencia libre
Desarrollado por la Django software foundation

Utilizado por Instagram, Disqus, Pinterest,Bitbucket,Udemy,NASA

Promueve el desarrollo ágil y extensible
Tiene un sistema de módulo reutilizables, las "apps"

Características notables:
Mapeador ORM para las bases de datos
Panel de administrador autogenerado
Sistema Plantillas extensibles
Soporta diferentes bases de datos SQL

Ideal para:
Autenticación de usuarios
Sesiones
Operaciones con ficheros
Mensajería
Plataformas de pago

No es lo mejor para: 
Manejar microservicios sin backend
Aplicaciones de Big Data
Plataformas con sockets en tiempo real

2- INSTALACIÓN CON PIPENV
En CMD: 
Instalación Django: pipenv
cd directorio proyecto
pip install pipenv
pipenv install django
pip install django==2.2.3
desinstalar un paquete : pipenv uninstall django

3-CREANDO EL PROYECTO
Utilizaremos este comando para crear el proyecto de nombre tutorial: pipenv run django-admin startproject tutorial

Probaremos a poner el servidor de django en marcha:
cd tutorial
pipenv run python manage.py runserver
Entramos en : http://127.0.0.1:8000, localhost: 127.0.0.1 en el puerto 8000, que es donde se está ejecutando django
Parar el servidor: ctrl+c
Si intentamos volver a acceder a la url anterior no podremos


Otra forma de poner el servidor en marcha: 
En Pipfile: 
[scripts]
server="python manage.py runserver"

En CMD:
pipenv run server (server es el nombre del script anterior)

4- CONFIGURACIÓN BÁSICA
Carpeta tutorial:
-__init__.py: Inicializa un paquete en un directorio y ejecuta código durante su importación.
No es obligatorio para manejar los paquetes desde Python 3.3.

-settings.py: Fichero principal de la configuración de Django.

-urls.py: Fichero donde se configuran las direcciones que van a escucharse en las peticiones url del navegador
127.0.0.1:8000/blog , blog es la url

-wsgi.py: Contiene la configuración de la interfaz wsgi para realizar el despliegue en servidores para entornos de producción.
Crea una variable aplication para manejar todo el servicio en marcha.

5- CREANDO UN BLOG

-Apps
pipenv run python manage.py startapp blog : blog es el nombre de la aplicación
Se crea una nueva carpeta llamada blog, y dentro hay varios ficheros.
Activamos la aplicación: tutorial/settings.py/
En INSTALLED_APPS, añadimos 'blog'.

-------------------------------------------------------------
-Modelos: clases donde se define la estructura de los datos
Dentro de models.py de la app blog.
class Post(models.Model):	
	title= models.CharField(max_length=200)
	content= models.TextField()

Trasladamos a la base de datos creando un registro de los cambios, creando la migración 0001_initial.py:
pipenv run python manage.py makemigrations
pipenv run manage.py migrate
Se crea la base de datos db.sqlite3 que podemos consultar con DBrowser for SQLite
Hay varios campos o tablas, y nos interesa sobre todo blog_post (inicialmente sin datos)

-------------------------------------------------------------
2 formas de editar el blog (administrador de django o shell)

- Panel de Administrador de Django
cd C:\Users\Daniel\CursoPython-Final\Django\tutorial
pipenv run server
Entramos en http://127.0.0.1:8000/admin
admin está definido en tutorial/urls.py
Aparece un formulario donde nos pide un usuario y una contraseña que inicialmente no tenemos y tendremos que crear
Creamos un superusuario: pipenv run python manage.py createsuperuser
usuario:admin y contraseña 1234 (no usar esto para un proyecto real)
Vamos a blog, admin..py y activamos el administrador:
from .models import Post
admin.site.register(Post)

Ahora veremos una nueva sección Blog y el modelo Posts en http://127.0.0.1:8000/admin/auth/user/
Podemos añadir nuevas entradas y editar algunas propiedades en models.py
Creamos una entrada de prueba (Post object (1))
Actualizamos DB Browser for SQLite y ahora vemos que la tabla blog_post tiene datos

-------------------------------------------------------------
-Shell (intérprete de comandos de django a través de objetos y métodos)
pipenv run python manage.py shell
from blog.models import Post
Post.objects.all() : lista las entradas de la base de datos
Post.objects.first() : lista la primera entrada
Post.objects.last(): lista la última entrada
Post.objects.get(id=3): Recuperar una entrada a partir de su identificador 3
Ej: http://127.0.0.1:8000/admin/blog/post/3/change/ (el 3 es el identificador)


Consultamos y editamos una entrada:
entrada= Post.objects.first()
entrada.title
entrada.content
entrada.title="He editado este título"
entrada.save()
entrada= Post.objects.create(title="Cuarta entrada",content="Texto de prueba")
entrada.delete()
quit()
-------------------------------------------------------------

-Vistas y url
Vistas definidas en urls.py con admin.site.urls:  path('admin/', admin.site.urls),
Una dirección url está enlazada a una vista en views.py (patrón:  modelo, vista, template)

Cramos una vista para manejar la portada:
En views.py:

def home(request): # Esta función se encarga de la vista en http://127.0.0.1:8000/ en texto plano
	return HttpResponse("Bienvenido a mi blog")


En urls.py:
from blog.views import home #blog es la app, home es la función de la vista de la portada creada en views.py

urlpatterns = [
path ('',home), # la ruta es la portada que no hace falta poner nada
]

Renderizar un template html bien estructurado:
blog/ nueva carpeta llamada templates y dentro otra llamada blog(nombre de la app)
Dentro de blog creamos los templates. Nuevo archivo llamada home.html
Dentro de home.html:
html:5 + tabulador y escribimos los que queramos en formato html
Cargamos la plantilla home.html en la vista def home:

def home(request): 
	return render (request, "blog/home.html") # renderizamos un template html home.html bien estructurado y no un texto plano

Ahora vamos a http://127.0.0.1:8000 
con control + u vemos el código html que hemos escrito
-------------------------------------------------------------
-Variables de contexto
en el fichero view.py
Cargamos: from .models import Post (.models está en el mismo directorio que views.py por eso soolo ponemos un punto delante )

Recuperamos las entradas dentro de la función home:

def home(request): # Renderizamos un template html home.html bien estructurado
	posts= Post.objects.all()
	return render (request, "blog/home.html",{'posts':posts}) # {} diccionario de contexto, clave 'posts' y el valor que devuelve es la lista de objetos llamada posts que contiene los mensajes recuperados de la base de datos, es decir las entradas o posts.

posts lo estamos enviando al template "blog/home.html", por lo que hay que acceder a esa información:
Recuperamos los datos que enviamos al diccionario de contexto.
{{posts}} <! etiqueta de django , no html, para mostrar variable de contexto del diccionario de contexto que recupera los datos de la base de datos>

Podemos jugar con los bucles como el for para ir mostrando esas entradas : 

<body text="RED">
		<h1>Bienvenido a mi blog</h1> <! título o encabezado>
		{% for post in posts %}
		<div>
			<h2> {{post}} </h2>
		</div>
		{% endfor %}
	</body>

Ahora en http://127.0.0.1:8000/ veremos las entradas apiladas. 
Vemos los títulos porque en models.py se devolvía el título: 
def __str__(self):
		return self.title


De esta forma veremos todo más claro, título y contenido : 
<h2> {{post.title}} </h2>
<p>{{post.content}} </p>
Hemos completado el flujo del patrón (modelo, vista, template), lo más importante de django
-------------------------------------------------------------
-Páginas dinámicas

Visualizamos las entradas individualmente, en lugar de tener las entradas en la portada
La clave esta en pasar un valor en la url a través del cual podamos recuperar el registro para renderizarlo.
Utilizaremos los identificadores de las entradas (id), ej: 127.0.0.1:8000/blog/1

En views.py:
def post(request,id):
	post= Post.objects.get(id=id)
	return render(request,"blog/post.html",{'posts':posts})

Copiamos el template home.html y le ponemos de nombre post.html, y editamos el código.
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>{{post.title}}</title> <! título de la ventana>
	</head>

	<body>
		<h1>{{post.title}} </h1>
		<p>{{post.content}} </p>
		
	</body>

</html>

En urls.py capturamos el id

from blog.views import home,post
urlpatterns = [
path('blog/<id>',post),
]

En views.py:
def post(request,id):
	post= Post.objects.get(id=id)
	return render(request,"blog/post.html",{'post':post})


si ponemos un identificador que no existe no saldrá el debug con información de los directorios,etc.
Poniendo el debug en false no se costrará esa info. 


Para ir desde la portada a las entradas:
En home.html:
cambiamos <p>{{post.content}} </p> por 
<p> <a href="/blog/{{post.pk}}"> Leer más </a></p> <! pk (primary key) hace referencia al ido, también se puede dejar como id>

web dinámica: el contenido se genera automáticamente a través de los datos de la base de datos, las entradas. 

"""
