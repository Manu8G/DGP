from django.contrib import admin
from .models import Profile, Friend
from .models import Usuario, Curso, Alumno, Profesor, Admin, Curso, Mensaje, Chat, Tarea, Comanda, Menu

# Register your models here.
admin.site.register([Profile, Friend])

admin.site.register(Usuario)

admin.site.register(Curso)

admin.site.register(Alumno)

admin.site.register(Profesor)

admin.site.register(Admin)

admin.site.register(Mensaje)

admin.site.register(Chat)

admin.site.register(Tarea)

admin.site.register(Comanda)

admin.site.register(Menu)


