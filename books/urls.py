
from django.urls import path
from . import views


urlpatterns = [
    path('', views.book_list_view, name='book_list'),
    path('<slug:slug>/', views.book_detail_view, name='book_detail'),
    path('<slug:slug>/read/', views.book_flip_view, name='book_flip'),
]
