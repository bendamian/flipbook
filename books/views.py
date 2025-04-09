
from django.shortcuts import render, get_object_or_404
from .models import Book, Category


def book_list_view(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


def book_detail_view(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'books/book_detail.html', {'book': book})


def book_flip_view(request, slug):
    book = get_object_or_404(Book, slug=slug)
    pages = book.pages.all()
    return render(request, 'books/flipbook.html', {'book': book, 'pages': pages})


