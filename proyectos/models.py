from django.db import models

class Habilidad(models.Model):
    nombre = models.CharField(max_length=100)
    experiencia = models.IntegerField(help_text="Años de experiencia")

    class Meta:
        ordering = ['nombre'] 

    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='proyectos/', blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    demo_url = models.URLField(blank=True, null=True)
    repo_url = models.URLField(blank=True, null=True)

    habilidades = models.ManyToManyField(Habilidad, related_name='proyectos')

    class Meta:
        ordering = ['fecha_publicacion']

    def __str__(self):
        return self.titulo


