from django.conf.urls import url
from . import views


app_name = 'indicie'

urlpatterns = [
    # indicie detail view
    url(r'^id/(?P<pk>[0-9]+)$', views.IndicieDetailView.as_view(), name='indicie-detail'),
]