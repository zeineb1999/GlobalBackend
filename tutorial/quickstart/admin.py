from django.contrib import admin
from .models import *

admin.site.register(Zone)
admin.site.register(Equipement)
admin.site.register(Etage)
admin.site.register(ExcelData)
admin.site.register(Batiment)
admin.site.register(PeriodeActivite)
admin.site.register(PeriodeActiviteLastYear)
admin.site.register(Alerte)
admin.site.register(ProfileUser)
admin.site.register(Rapport)
admin.site.register(Sauvegarde)
admin.site.register(Historique)
admin.site.register(HistoriqueUser)
admin.site.register(EquipementArchive)
admin.site.register(HistoriqueADbatiment)
admin.site.register(HistoriqueADetage)
admin.site.register(HistoriqueADzone)
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']


