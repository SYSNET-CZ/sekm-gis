from django.contrib.gis import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import IndicieDpz

admin.site.register(IndicieDpz, admin.GeoModelAdmin)
class IndicieAdmin(OSMGeoAdmin):
    list_display = ('indic_id', 'geom')
