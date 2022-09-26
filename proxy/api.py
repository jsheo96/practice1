import requests
def weather_location(location):
    appid = '021df3c26d34083f1320505e684679ed'
    latitude = location.latitude
    longitude = location.longitude
    service_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'lat': latitude, 'lon': longitude, 'appid': appid}
    res = requests.get(service_url, params=params)
    j = res.json()
    return j