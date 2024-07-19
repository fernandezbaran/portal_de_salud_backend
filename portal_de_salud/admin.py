from django.contrib import admin
from portal_de_salud.models import Pacientes,Medicacion,Imagenes,Contact

class PacientesAdmin(admin.ModelAdmin):
	list_display=("nombre","direccion","telefono",)
	search_fields=("nombre","telefono",)

class MedicacionAdmin(admin.ModelAdmin):
	list_filter=("droga",)

class ImagenesAdmin(admin.ModelAdmin):
	list_display=("estudio","diagnostico",)
	list_filter=("estudio",)

admin.site.register(Pacientes, PacientesAdmin)
admin.site.register(Medicacion,MedicacionAdmin)
admin.site.register(Imagenes,ImagenesAdmin)
admin.site.register(Contact)
