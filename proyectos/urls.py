from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_proyecto, name='lista_proyecto'),
    path('proyecto/nuevo/', views.crear_proyecto, name='crear_proyecto'),
    path('proyecto/<int:pk>/editar/', views.editar_proyecto, name='editar_proyecto'),
    path('proyecto/<int:pk>/eliminar/', views.eliminar_proyecto, name='eliminar_proyecto'),
    path('registro/', views.registro_usuario, name='registro'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
]