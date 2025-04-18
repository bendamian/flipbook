# project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # 👈 This line includes your book viewer URLs
    path('books/', include('books.urls')),
    path('gallery/', include('gallery.urls')),
    path('video/', include('video.urls')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)



