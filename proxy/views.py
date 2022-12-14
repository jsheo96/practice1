from django.shortcuts import render, redirect
from .models import Location
from .forms import LocationForm
from .api import weather_location
from django.http import JsonResponse
from crawling import do_crawl
from crawling import crawl_url_list
from rest_framework import viewsets
from rest_framework import permissions
from .models import Aquainfo
from .serializers import AquainfoSerializer
# Create your views here.
#def submit_view(request):
#    return render(request, 'proxy/submit.html')

def aqua_notice_page(request):
    data = crawl_url_list()
    return render(request, 'proxy/aqua_notice.html', data)

def aqua_notice_view(request):
    data = crawl_url_list()
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})

def sealife_view(request):
    data = do_crawl()
    print(data)
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})

def weather_view(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            location = Location()
            location.latitude = form.cleaned_data['latitude']
            location.longitude = form.cleaned_data['longitude']
            j = weather_location(location)
            params = {}
            params['lat'] = location.latitude
            params['lon'] = location.longitude
            params['temp'] = int(j['main']['temp'] - 273.15)
            params['humidity'] = j['main']['humidity']
            params['sea_level'] = j['main']['sea_level']
            params['wind_speed'] = j['wind']['speed']
            params['wind_direction'] = j['wind']['deg']

            return render(request, 'proxy/weather.html', params)
    print('weather_view!!')
    return render(request, 'proxy/weather.html', {'location': location})

def submit_view(request):
    form = LocationForm()
    return render(request, 'proxy/submit.html', {'form': form})

class AquainfoViewSet(viewsets.ModelViewSet):
    queryset = Aquainfo.objects.all()
    serializer_class = AquainfoSerializer
    # permission_classes = [permissions.AllowAny]
