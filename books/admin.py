from django.contrib import admin
from .models import Book, Page


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('book', 'page_number')
