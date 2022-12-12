from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Usuario(models.Model):
    usuario     = models.CharField(max_length = 10)
    password    = models.CharField(max_length = 30)

    def __str__(self):
        return self.usuario

class Curso(models.Model):
    id_curso    = models.CharField(max_length = 10)

    def __str__(self):
        return self.id_curso


class Alumno(models.Model):
    nombre              = models.CharField(max_length = 10)
    user                = models.OneToOneField(User, on_delete=models.CASCADE)
    pic                 = models.ImageField(upload_to="img", blank=True, null=True)
    id_curso            = models.ForeignKey(Curso, on_delete = models.CASCADE)
    usuario_pictograma  = models.BooleanField(default = False)
    tipo_discapacidad   = models.CharField(max_length = 20)

    def __str__(self):
        return self.nombre


class Profesor(models.Model):
    nombre              = models.CharField(max_length = 10)
    user                = models.OneToOneField(User, on_delete=models.CASCADE)
    pic                 = models.ImageField(upload_to="img", blank=True, null=True)
    id_curso            = models.ForeignKey(Curso, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre


class Image(models.Model):
    id_image        = models.CharField(max_length = 10)
    ruta            = models.CharField(max_length = 140)

    def __str__(self):
        return self.id_image


class ImageList(models.Model):
    id_image_list        = models.CharField(max_length = 20)
    images_id            = models.ManyToManyField(Image)

    def __str__(self):
        return self.id_image_list


class Tarea(models.Model):
    id_tarea    = models.CharField(max_length = 10)
    tipo_tarea  = models.CharField(max_length = 20)
    descripcion = models.CharField(max_length = 140)
    image_list  = models.ForeignKey(ImageList, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.id_tarea


class Comanda(models.Model):
    id_tarea    = models.ForeignKey(Tarea, on_delete = models.CASCADE)
    material    = models.CharField(max_length = 20)
    cantidad    = models.IntegerField()
    aula        = models.CharField(max_length = 10)

    def __str__(self):
        return self.id_tarea.id_tarea


class Menu(models.Model):
    id_tarea        = models.ForeignKey(Tarea, on_delete = models.CASCADE)
    tipo            = models.CharField(max_length = 20)
    postre          = models.CharField(max_length = 140)
    cantidad        = models.IntegerField()
    cantidad_postre = models.IntegerField()

    def __str__(self):
        return self.id_tarea.id_tarea


