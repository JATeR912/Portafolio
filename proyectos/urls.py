from django.urls import path
from . import views
from .views import index, lista_habilidades, lista_proyecto, detalle_proyecto, crear_proyecto, eliminar_proyecto, editar_proyecto, consulta_sql, contacto,  login_usuario, logout_usuario

urlpatterns = [
    path('', views.index, name='index'),
    path('habilidades/', views.lista_habilidades, name='lista_habilidades'),
    path('contacto/', views.contacto, name='contacto'),

    # PROYECTOS
    path('proyecto/', views.lista_proyecto, name='lista_proyecto'),
    path('proyecto/<int:pk>/detalle/', views.detalle_proyecto, name='detalle_proyecto'),
    path('proyecto/nuevo/', views.crear_proyecto, name='crear_proyecto'),
    path('proyecto/<int:pk>/editar/', views.editar_proyecto, name='editar_proyecto'),
    path('proyecto/<int:pk>/eliminar/', views.eliminar_proyecto, name='eliminar_proyecto'),
    path('proyecto/sql/', views.consulta_sql, name="consulta_sql"),

    # AUTH
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
]