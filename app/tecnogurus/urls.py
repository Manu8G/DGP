from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chat_rooms', views.chat_rooms, name='chat_rooms'),
    path('room/<str:room_name>/', views.room, name="room"),
    path('login_picto', views.login_picto, name='login_picto'),
    path('buscador.html', views.buscador, name='buscador'),
    path('login_ok.html', views.login_ok, name='login_ok'),
    path('failed_login.html', views.failed_login, name='failed_login'),
    path('request_login.html', views.request_login, name='request_login'),
    path('prueba', views.prueba, name='prueba'),
    path('fin_tarea', views.fin_tarea, name='fin_tarea'),
    path('borrar_tarea', views.borrar_tarea, name='borrar_tarea'),
    path('<str:id_tarea>/modificarTarea', views.modificarTarea, name='modificarTarea'),
    path('crearTarea', views.crearTarea, name='crearTarea'),
    path('listaTarea', views.listaTarea, name='listaTarea'),
    path('<str:id_image_list>/listaImagenes', views.listaImagenes, name='listaImagenes'),
    path('creaListaImagenes', views.creaListaImagenes, name='creaListaImagenes'),
]
