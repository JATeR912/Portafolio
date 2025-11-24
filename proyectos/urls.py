from django.urls import path
from . import views
from .views import index, lista_proyectos, detalle_proyecto, crear_proyecto, eliminar_proyecto, editar_proyecto, consulta_sql

urlpatterns = [
    path('', views.index, name='index'),

    # PROYECTOS
    path('proyecto/', views.lista_proyecto, name='lista_proyecto'),
    path('proyecto/<int:pk>/detalle/', views.detalle_proyecto, name='detalle_proyecto'),
    path('proyecto/nuevo/', views.crear_proyecto, name='crear_proyecto'),
    path('proyecto/<int:pk>/editar/', views.editar_proyecto, name='editar_proyecto'),
    path('proyecto/<int:pk>/eliminar/', views.eliminar_proyecto, name='eliminar_proyecto'),
    path('proyecto/sql/', views.consulta_sql, name="consulta_sql"),

    # AUTH
    path('registro/', views.registro_usuario, name='registro'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
]