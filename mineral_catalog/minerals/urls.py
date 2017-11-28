from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.mineral_list, name='list'),
    url(r'search/$', views.search, name='search'),
    url(r'(?P<pk>\d+)/$', views.mineral_detail, name='detail'),
]