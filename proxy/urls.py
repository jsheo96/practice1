from django.conf.urls import url
from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include
router = DefaultRouter()
router.register(r'aquainfo', views.AquainfoViewSet,basename="aquainfo")

urlpatterns = [
    url('submit/', views.submit_view, name='submit'),
    url('weather/', views.weather_view, name='weather'),
    url('sealife/', views.sealife_view, name='sealife'),
    url('aqua_notice/', views.aqua_notice_view, name='aqua_notice'),
    url('aqua_notice_page/', views.aqua_notice_page, name='aqua_notice_page'),
    # url('aquainfo/', views.AquainfoViewSet.as_view(), name='aquainfo'),
    url('', include(router.urls))
]
