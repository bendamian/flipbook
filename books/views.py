
from django.urls import path
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Book


# Create your views here.


def book_flip_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    pages = book.pages.all()
    return render(request, 'books/flipbook.html', {'book': book, 'pages': pages})



