from django.shortcuts import render, get_object_or_404, redirect
from django.db import connection
from .models import Proyecto, Habilidad
from .forms import ProyectoForm, RegistroForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

#INDEX
def index(request):
    return render(request, "index.html")

# LISTA DE HABILIDADES
def lista_habilidades(request):
    habilidades_tecnicas = Habilidad.objects.filter(tipo='tecnica')
    habilidades_blandas = Habilidad.objects.filter(tipo='blanda')

    context = {
        "habilidades_tecnicas": habilidades_tecnicas,
        "habilidades_blandas": habilidades_blandas,
    }
    return render(request, "habilidades.html", context)

# LISTA DE PROYECTOS
def lista_proyecto(request):
    proyecto = Proyecto.objects.all().order_by('-fecha_publicacion')
    return render(request, "proyectos/lista_proyecto.html", {"proyecto": proyecto})


# DETALLE DE PROYECTO
def detalle_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    return render(request, "proyectos/detalle_proyecto.html", {"proyecto": proyecto})

# --- CRUD restringido al admin del proyecto ---
# CREAR PROYECTO
@login_required
def crear_proyecto(request):
    if not request.user.is_staff:
        raise PermissionDenied
    if request.method == "POST":
        form = ProyectoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proyecto creado correctamente.')
            return redirect("lista_proyecto")
    else:
        form = ProyectoForm()
    return render(request, "proyectos/crear_proyecto.html", {"form": form})

# EDITAR PROYECTO
@login_required
def editar_proyecto(request, pk):
    if not request.user.is_staff:
        raise PermissionDenied
    proyecto = get_object_or_404(Proyecto, pk=pk)
    form = ProyectoForm(request.POST or None, request.FILES or None, instance=proyecto)
    if form.is_valid():
        form.save()
        messages.success(request, 'Proyecto actualizado.')
        return redirect('detalle_proyecto', pk=proyecto.pk)
    return render(request, 'proyectos/editar_proyecto.html', {'form': form, 'proyecto': proyecto})

# ELIMINAR PROYECTO
@login_required
def eliminar_proyecto(request, pk):
    if not request.user.is_staff:
        raise PermissionDenied
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == 'POST':
        proyecto.delete()
        messages.warning(request, 'Proyecto eliminado correctamente.')
        return redirect('lista_proyecto')
    return render(request, 'proyectos/eliminar_proyeto.html', {'proyecto': proyecto})

# CONSULTA SQL 
@login_required
def consulta_sql(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT p.id, p.titulo, h.nombre, h.experiencia
            FROM proyectos_proyecto p
            JOIN proyectos_proyecto_habilidades ph ON p.id = ph.proyecto_id
            JOIN proyectos_habilidad h ON h.id = ph.habilidad_id
            ORDER BY p.fecha_publicacion DESC;
        """)
        resultados = cursor.fetchall()

    return render(request, "proyectos/sql_proyecto.html", {"resultados": resultados})

# CONTACTO
def contacto(request):
    return render(request, "contacto.html")

# AUTENTICACIÓN DE USUARIO

def es_admin_proyecto(user):
    return user.is_staff  


# --- Autenticación ---
def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'Bienvenido {user.username}')
            return redirect('lista_proyecto')
        else:
            messages.error(request, 'Credenciales inválidas')
    return render(request, 'login.html')

@login_required
def logout_usuario(request):
    logout(request)
    messages.info(request, 'Sesión cerrada correctamente.')
    return render(request, 'logout.html')

# --- Errores personalizados ---
def error_403(request, exception=None):
    return render(request, '403.html', status=403)

def error_404(request, exception=None):
    return render(request, '404.html', status=404)