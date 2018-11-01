from django.conf.urls import include, url
from django.urls import path, include
from .views import register

from . import views



urlpatterns = [
	#INICIO
    url(r'^$', views.inicio),
    #URLOGIN 
    url('perris/login', views.login , name="login"),
    #Perros Disponibles
    url('perris/disponibles', views.perros_disponibles , name="perros_disponibles"),
    url('administrador',views.administrador_inicio, name="adm.inicio" ),
    #Agregar un nuevo post del perro_rescatado 
    path('agregar', views.new_post_perro, name='new_post_perro'),
    #Eliminar post 
    
    path('eliminar/<int:pk>', views.delete_post_perro, name='delete_post_perro'),
    #Detalles del post
    url(r'^perro/(?P<pk>[0-9]+)/$', views.detail_post_perro,name='detail_post_perro'),
    #Editar un Post del Perro Rescatado 
    
    path('perro/<int:pk>/editar/', views.edit_post_perro, name='edit_post_perro'),

    url(r'^form/', views.form, name='form'),

    url(r'^register/', views.register, name= "register"),

]

