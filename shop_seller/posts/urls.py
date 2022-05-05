from django.urls import path
from .views import default_map, process_url_from_client,check_my_info

urlpatterns = [
    path('', default_map, name="index" ),
    path('send_my_cord/', process_url_from_client ,name='send_my_cord'),
    path('check/', check_my_info, name='check')
]