from django.contrib import admin
from .models import Book, Category, Page


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_name', 'category', 'uploaded_at')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('category', 'uploaded_at')
    search_fields = ('title', 'author_name', 'description')
    readonly_fields = ('uploaded_at',)
    ordering = ('-uploaded_at',)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('book', 'page_number')
    list_filter = ('book',)
    ordering = ('book', 'page_number')
