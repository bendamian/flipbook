from .utils.pagination import paginate_queryset
from django.shortcuts import render
from .models import Book, Category
from django.shortcuts import render, get_object_or_404


def book_list_view(request):
    books = Book.objects.order_by('-uploaded_at')  # or .order_by('title') etc.
    paginated_books = paginate_queryset(request, books, per_page=16)
    return render(request, 'books/book_list.html', {'books': paginated_books})

def book_detail_view(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'books/book_detail.html', {'book': book})


def book_flip_view(request, slug):
    book = get_object_or_404(Book, slug=slug)
    pages = book.pages.all()
    return render(request, 'books/flipbook.html', {'book': book, 'pages': pages})


