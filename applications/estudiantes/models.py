from django.db import models
from applications.carreras.models import Carrera

# Create your models here.
class Estudiante(models.Model):
    listMatriculas = [('0','Primera'),
                    ('1','Segunda'),
                    ('2','Tercera')]
    nameStudent = models.CharField(max_length=40, blank=False, null=False)
    lastNameStudent = models.CharField(max_length=40, blank=False, null=False)
    dniStudent = models.CharField(max_length=10, blank=False, null=False)
    matStudent = models.CharField(max_length=1, blank=False, null=False, choices=listMatriculas)
    emailStudent = models.EmailField(max_length=100, blank=False, null=False)
    carrerStudent = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='estudiantes', null=True, blank=False)

    def __str__(self):
        return self.dniStudent + ' - ' + self.nameStudent

    class Meta:
        verbose_name = "Alumnado"
        verbose_name_plural = "Lista de estudiantes"
        ordering = ["lastNameStudent"]