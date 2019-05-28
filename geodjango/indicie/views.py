from django.shortcuts import render

# Create your views here.

from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from .models import IndicieDpz
from django.contrib.gis.geos import Point

x = -770161.02315189654
y = -1068535.5028360416

user_location = Point(x, y, srid=5514)

class Home(generic.ListView):
    model = IndicieDpz
    context_object_name = 'indicie_list'
    queryset = IndicieDpz.objects.annotate(distance=Distance('geom', user_location)).order_by('distance')[0:6]
    template_name = 'indicie/index.html'

class IndicieDetailView(generic.DetailView):
    model = IndicieDpz
    template_name = 'indicie/detail.html'
