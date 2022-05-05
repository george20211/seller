from django.shortcuts import render
import folium
import geocoder
from api.views import get_a_seat
from .models import Trashed
from django.contrib.auth.decorators import login_required

@login_required
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

@login_required
def process_url_from_client(request):
    long = request._post['long']
    shrt = request._post['shrt']
    inf = get_a_seat(long, shrt)
    print(inf)
    if Trashed.objects.filter(user=request.user).exists():
        Trashed.objects.filter(user=request.user).delete()
    Trashed.objects.create(user=request.user, trololo=inf)
    return render(request, 'test_open.html', {'inf': inf})

def check_my_info(request):
    inf = Trashed.objects.get(user=request.user)
    return render(request, 'test_open.html', {'inf': inf})