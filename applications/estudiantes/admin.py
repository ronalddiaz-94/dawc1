from django.contrib import admin

from .models import Estudiante

class EstudianteAdmin(admin.ModelAdmin):
    list_display = (
        "nameStudent",
        "lastNameStudent",
        "dniStudent",
        "matStudent",
        "emailStudent",
        "carrerStudent",
        "id",
    )
    list_filter= ("carrerStudent", "matStudent",)
    search_fields = ("nameStudent",)

admin.site.register(Estudiante, EstudianteAdmin)
