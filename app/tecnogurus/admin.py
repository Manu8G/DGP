from django.contrib import admin
from .models import Curso, Alumno, Profesor, Curso, Tarea, Comanda, Menu, Image, ImageList

# Register your models here.

admin.site.register(Image)

admin.site.register(ImageList)

admin.site.register(Curso)

admin.site.register(Alumno)

admin.site.register(Profesor)

admin.site.register(Tarea)

admin.site.register(Comanda)

admin.site.register(Menu)


