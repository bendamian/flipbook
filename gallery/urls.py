from django.urls import path
from .views import album_detail, album_list

urlpatterns = [
    path('', album_list, name='album_list'),
    path('album/<int:album_id>/', album_detail, name='album_detail'),
]
