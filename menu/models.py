from django.db import models

# Create your models here.
class Wiki(models.Model):
    id = models.AutoField(primary_key=True)
    wiki = models.CharField(max_length=30)
    context = models.TextField(null=True, blank=True,max_length=100)

    def __str__(self):
        return self.wiki

class Campo(models.Model):
    id = models.AutoField(primary_key=True)
    wiki = models.ForeignKey(Wiki, on_delete=models.CASCADE)
    campos = models.CharField(max_length=50)
    def __str__(self):
        return self.campos

class Descripcion_campo(models.Model):
    id = models.AutoField(primary_key=True)
    campo = models.ForeignKey(Campo, on_delete=models.CASCADE)
    imagen = models.CharField(max_length=50)
    mensaje = models.CharField(max_length=50)
    def __str__(self):
        return self.mensaje

class Descripcion(models.Model):
    id = models.AutoField(primary_key=True)
    wiki = models.ForeignKey(Wiki, on_delete=models.CASCADE)
    imagen = models.CharField(max_length=50)
    mensaje = models.CharField(max_length=50)
    def __str__(self):
        return self.mensaje