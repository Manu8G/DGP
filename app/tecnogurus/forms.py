# from socket import fromshare
from django import forms
from django.forms import ModelForm
from .models import  Tarea, ImageList


class modificarTareaForm(ModelForm):
   class Meta:
        model = Tarea
        fields = ["tipo_tarea","descripcion","image_list"]
   '''
   image_list = forms.ModelMultipleChoiceField(
        queryset=ImageList.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )'''
        
class crearTareaForm(ModelForm):
   class Meta:
        model = Tarea
        fields = ["id_tarea","tipo_tarea","descripcion", "image_list"]
   '''
   image_list = forms.ModelMultipleChoiceField(
        queryset=ImageList.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )'''