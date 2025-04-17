from django.db import models

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=30)
    password = models.CharField(max_length=250)
    def __str__(self):
        return self.usuario