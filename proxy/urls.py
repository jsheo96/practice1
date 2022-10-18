from django.conf.urls import url
from . import views
urlpatterns = [
    url('submit/', views.submit_view, name='submit'),
    url('weather/', views.weather_view, name='weather'),
    url('sealife/', views.sealife_view, name='sealife'),
    url('aqua_notice/', views.aqua_notice_view, name='aqua_notice'),
    url('aqua_notice_page/', views.aqua_notice_page, name='aqua_notice_page'),
]
