from django.contrib import admin

from apps.alumna.models import antecedentes_medicos, Alumna

# Register your models here.

admin.site.register(antecedentes_medicos)
admin.site.register(Alumna)
