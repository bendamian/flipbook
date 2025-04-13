from django.urls import path
from .views import video_list_view, video_detail_view

urlpatterns = [
    path('', video_list_view, name='video_list'),
    path('<slug:slug>/', video_detail_view, name='video_detail'),
]
