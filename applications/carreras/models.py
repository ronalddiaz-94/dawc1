from django.db import models

# Create your models here.
class Carrera(models.Model):
    nameCarrer = models.CharField(blank=False, null=False, max_length=50)
    fundationCarrer = models.CharField(blank=False, null=False, max_length=100)

    def __str__(self):
        return str(self.id) + '-' + self.nameCarrer

    class Meta:
        verbose_name = "FACULTAD CIENCIA E INGENIERIA"
        verbose_name_plural = "Lista de carreras"
        ordering = ["-nameCarrer"]
