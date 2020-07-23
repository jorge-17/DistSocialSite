from django.contrib import admin
from .models import CatTipos, CatOrganizaciones, CatUsuarios, CatLocalidades, CatCamaras, Registros

# Register your models here.
admin.site.register(CatTipos)
admin.site.register(CatOrganizaciones)
admin.site.register(CatUsuarios)
admin.site.register(CatLocalidades)
admin.site.register(CatCamaras)
admin.site.register(Registros)