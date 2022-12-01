from django.contrib import admin
<<<<<<< HEAD
from .models import Profile, Friend
from .models import Usuario, Curso, Alumno, Profesor, Admin, Curso, Mensaje, Chat, Tarea, Comanda, Menu

# Register your models here.
admin.site.register([Profile, Friend])
=======
from .models import Curso, Alumno, Profesor, Curso, Tarea, Comanda, Menu

# Register your models here.
>>>>>>> prueba_luis


admin.site.register(Curso)

admin.site.register(Alumno)

admin.site.register(Profesor)

admin.site.register(Tarea)

admin.site.register(Comanda)

admin.site.register(Menu)


