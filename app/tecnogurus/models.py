from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    pic = models.ImageField(upload_to="img", blank=True, null=True)
    friends = models.ManyToManyField('Friend', related_name = "my_friends")
    
    def __str__(self):
        return self.name
    
    
class Friend(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.profile.name

class ChatMessage(models.Model):
    body = models.TextField()
    msg_sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="msg_sender")
    msg_receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="msg_receiver")
    seen = models.BooleanField(default=False)
    
    def __str__(self):
        return self.body
# ESTABA De aqui para abajo ya estaba

class Usuario(models.Model):
    usuario     = models.CharField(max_length = 10)
    password    = models.CharField(max_length = 30)

    def __str__(self):
        return self.usuario


class Curso(models.Model):
    id_curso    = models.CharField(max_length = 10)
    tutor       = models.CharField(max_length = 10)

    def __str__(self):
        return self.id_curso


class Alumno(models.Model):
    usuario             = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    id_curso            = models.ForeignKey(Curso, on_delete = models.CASCADE)
    usuario_pictograma  = models.BooleanField(default = False)
    tipo_discapacidad   = models.CharField(max_length = 20)

    def __str__(self):
        return self.usuario.usuario


class Profesor(models.Model):
    usuario     = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    id_curso    = models.CharField(max_length = 10)

    def __str__(self):
        return self.usuario.usuario


class Admin(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)

    def __str__(self):
        return self.usuario.usuario


class Chat(models.Model):
    id_chat = models.CharField(max_length = 10)

    def __str__(self):
        return self.id_chat


class Mensaje(models.Model):
    id_mensaje  = models.CharField(max_length = 10)
    id_chat     = models.ForeignKey(Chat, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.id_mensaje


class Tarea(models.Model):
    id_tarea    = models.CharField(max_length = 10)
    tipo_tarea  = models.CharField(max_length = 20)
    descripcion = models.CharField(max_length = 140)
    id_mensaje  = models.ForeignKey(Mensaje, on_delete = models.CASCADE)

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
