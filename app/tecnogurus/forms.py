# from socket import fromshare
from django import forms
from django.forms import ModelForm
from .models import  Tarea, ImageList, Image, Alumno


class CustomMMCF(forms.ModelMultipleChoiceField):    
   def label_from_instance(self, Alumno):
        return "%s" % Alumno 


class modificarTareaForm(ModelForm):
   alumnos = []
   alumn = Alumno.objects.all()
   for a in alumn:
      alumnos.append(a)

   class Meta:
        model = Tarea
        fields = ["tipo_tarea","descripcion","image_list", "encargado"]
        

   encargado = forms.Select(choices=alumnos)

class crearTareaForm(ModelForm):
   alumnos = []
   alumn = Alumno.objects.all()
   for a in alumn:
      alumnos.append(a)

   class Meta:
        model = Tarea
        fields = ["id_tarea","tipo_tarea","descripcion", "image_list", "encargado"]

   encargado = forms.Select(choices=alumnos)

class creaListaImagenesForm(ModelForm):
   class Meta:
        model = ImageList
        fields = ["id_image_list","images_id"]

