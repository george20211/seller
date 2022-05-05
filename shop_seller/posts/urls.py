from django.urls import path
from .views import default_map, process_url_from_client

urlpatterns = [
    path('', default_map, name="index" ),
    path('send_my_cord/', process_url_from_client ,name='send_my_cord')
]