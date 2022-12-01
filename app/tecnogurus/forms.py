# from socket import fromshare
from django import forms
from django.forms import ModelForm
from .models import  Tarea


class modificarTareaForm(ModelForm):
   class Meta:
        model = Tarea
        fields = ["tipo_tarea","descripcion"]
        
class crearTareaForm(ModelForm):
   class Meta:
        model = Tarea
        fields = ["id_tarea","tipo_tarea","descripcion"]
