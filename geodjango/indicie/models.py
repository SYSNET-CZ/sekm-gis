from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

from django.contrib.gis.gdal import SpatialReference, CoordTransform

class IndicieDpz(models.Model):
    # Indicie NIKM
    # GeoDjango-specific: a geometry field (MultiPolygonField)
    geom = models.MultiPointField(srid=5514, blank=True, null=True)
    # _wgs = models.PointField(srid=4326, blank=True, null=True, default=None, db_column="wgs")

    typ = models.CharField(max_length=3, blank=True, null=True)
    revize = models.CharField(max_length=1, blank=True, null=True)
    koment = models.CharField(max_length=68, blank=True, null=True)
    indicie = models.CharField(max_length=1, blank=True, null=True)
    indic_id = models.IntegerField(blank=True, null=True)
    xcoord = models.FloatField(blank=True, null=True)
    ycoord = models.FloatField(blank=True, null=True)
    nazev_orp = models.CharField(max_length=192, blank=True, null=True)
    charorp = models.CharField(max_length=6, blank=True, null=True)
    kod_ku_p = models.CharField(max_length=6, blank=True, null=True)
    naz_ku_p = models.CharField(max_length=40, blank=True, null=True)
    kod_obec_p = models.CharField(max_length=6, blank=True, null=True)
    naz_obec_p = models.CharField(max_length=40, blank=True, null=True)
    lau1_p = models.CharField(max_length=6, blank=True, null=True)
    naz_lau1_p = models.CharField(max_length=40, blank=True, null=True)
    cznuts3 = models.CharField(max_length=6, blank=True, null=True)
    naz_cnuts3 = models.CharField(max_length=40, blank=True, null=True)
    poznamka = models.CharField(max_length=254, blank=True, null=True)
    kod_orp = models.BigIntegerField(blank=True, null=True)
    id_orp = models.BigIntegerField(blank=True, null=True)
    stav = models.IntegerField(blank=True, null=True)

    @property
    def wgs(self):
        coord_wgs = SpatialReference(4326)
        coord_jtsk = SpatialReference(5514)
        trans = CoordTransform(coord_jtsk, coord_wgs)
        pnt = Point(self.xcoord, self.ycoord, srid=5514)
        pnt.transform(trans)
        # self._wgs = pnt
        # self.save(update_fields=["_wgs"]
        return pnt

    class Meta:
        managed = False
        db_table = 'indicie-dpz'
        ordering = ('indic_id',)
        verbose_name_plural = 'indicie'



