from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.truck_table, name='truck_table'),
]
