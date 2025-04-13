from .models import Album
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator


def album_list(request):
    albums = Album.objects.all().order_by('-created_at')
    paginator = Paginator(albums, 6)  # Show 6 albums per page
    page_number = request.GET.get('page')
    album_page = paginator.get_page(page_number)
    return render(request, 'gallery/album_list.html', {'album_page': album_page})



def album_detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'gallery/album_detail.html', {'album': album})
