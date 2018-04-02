# README
 
## Instalación
### 1. Instalar python 3.6.4
```
(mac)$ brew install python
(linux)$ apt-get install python-dev
(windows) descargar en [python](https://www.python.org)
```
### 2. Instalar virtualenv
```
	$ sudo pip install virtualenv
```
### 3. Crear entorno virtual
```
	$ virtualenv ENV
```
### 4. Iniciar entorno virtual
```
	$ source ENV/bin/activate
```
### Instalar Django
#### Clonando el proyecto
```
	(ENV)$ pip install -r requirements.txt
```

### Ejecutar proyecto
```
	$ python manage.py runserver
```
## Para crear un proyecto nuevo en Django
Seguir hasta el paso 4, luego continuar acá
1. Instalar Django
```
	(ENV)$ pip install django
```
2. Ubicarse en la carpeta donde quieres iniciar el proyecto 
```
	(ENV)$ django-admin startproject -nombre_proyecto-
```
3. Crear aplicacion
```
	(ENV)$ python manage.py startapp -nombre_apps-
```
4. Aplicar migraciones principales
```
	(ENV)$ pyhon manage.py migrate
```
5. Después de crear los modelos en `models.py` crear las migraciones
```
	(ENV)$ python manage.py makemigrations
```
6. En modo prueba se creo el archivo fixture/initial.json con datos iniciales
7. Se carga este archivo
```
	(ENV)$ python manage.py loaddata initial.json
```
8. Las vistas se crean en `views.py` y deben se incluidas en `urls.py` para poder acceder a ellas