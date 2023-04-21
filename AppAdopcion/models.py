from django.db import models


class Mascota(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.CharField(max_length=8)
    genero = models.CharField(max_length=6)
    vacunas = models.CharField(max_length=20)
    condicion_medica = models.CharField(max_length=20)
    castrado_a = models.CharField(max_length=2)
    foto = models.ImageField(upload_to="imagenes", null=True)

    def __str__(self):
        return self.nombre


class Comentario(models.Model):
    comentario = models.ForeignKey(Mascota, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=30)
    mensaje = models.TextField(null=True, blank=True)
    fechaComent = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComent']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)
