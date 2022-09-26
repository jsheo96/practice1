from django.conf.urls import url
from . import views
urlpatterns = [
    url('submit/', views.submit_view, name='submit'),
    url('weather/', views.weather_view, name='weather'),
]