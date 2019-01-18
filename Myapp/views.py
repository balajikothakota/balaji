# Create your views here.
from django.shortcuts import render
import requests


def home(request):
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
    print ip_address
    response = requests.get('http://api.ipstack.com/103.81.95.21?access_key=41af9020ffffca12a030dc7efbc51ac7%s' % ip_address)
    geodata = response.json()
    print geodata
    return render(request, 'home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'latitude': geodata['latitude'],
        'longitude': geodata['longitude'],
        'api_key': '41af9020ffffca12a030dc7efbc51ac7'  # Don't do this! This is just an example. Secure your keys properly.
    })
