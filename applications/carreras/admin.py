from django.contrib import admin

from .models import Carrera

class CarreraAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nameCarrer",
        "fundationCarrer",
    )
    list_filter= ("fundationCarrer",)
    search_fields = ("nameCarrer",)


admin.site.register(Carrera, CarreraAdmin)