from django.shortcuts import render
import folium
import geocoder
from api.views import get_a_seat

def default_map(request):
    xxx = request.POST.get('x')
    location = geocoder.osm('RUS')
    lat = location.lat
    lng = location.lng
    city = location.city
    m = folium.Map(location=[19, -12], zoom_start=10)
    folium.Marker([lat, lng], tooltip='Нажми на меня', popup=city).add_to(m)
    m = m._repr_html_()
    context = {
        'm':m,
    }
    return render(request, 'index.html', context)

def process_url_from_client(request):
    long = request._post['long']
    shrt = request._post['shrt']
    print(get_a_seat(long, shrt), 111111111111111111)
    return render(request, 'index.html')

