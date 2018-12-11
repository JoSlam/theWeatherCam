from django.conf.urls import url
from . import views

app_name = 'weather'

urlpatterns = [
    #/api/
    url(r'^$', views.index, name='index'),

    #/api/chart
    url(r'^chart/$', views.chart, name="chart"),

    #/api/chart_data
    url(r'^chart_data/$', views.chart_data, name='chart_data'),

    #/api/gallery   still needs work
    url(r'^gallery/$', views.gallery, name='gallery'),

    #/api/gallery/<image_id>
    url(r'^gallery/(?P<image_id>[0-9]+)$', views.image_details, name='image_details'),

    #/api/all
    url(r'^all/$', views.show_all, name='show_all'),

    #/api/archive
    url(r'^archive/$', views.archive, name='archive_data'),

    #/api/upload_cities
    url(r'^upload_cities/$', views.CityUploadView.as_view(), name='upload_cities'),
]
