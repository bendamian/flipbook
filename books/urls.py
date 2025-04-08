
from django.urls import path
from .views import book_flip_view

urlpatterns = [
    path('<int:book_id>/', book_flip_view, name='book_flip'),
]
