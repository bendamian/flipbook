from django.contrib import admin
from .models import Video, Category


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'uploaded_at']
    list_filter = ['category', 'uploaded_at', 'age_groups']
    search_fields = ['title', 'description']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'created_at']
    search_fields = ['name']
