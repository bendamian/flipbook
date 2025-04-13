from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Video, Category


def video_list_view(request):
    category_slug = request.GET.get('category')
    videos = Video.objects.all().order_by('-uploaded_at')
    categories = Category.objects.all()

    selected_category = None
    if category_slug:
        selected_category = get_object_or_404(Category, slug=category_slug)
        videos = videos.filter(category=selected_category)

    paginator = Paginator(videos, 8)  # 8 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'videos': page_obj,
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'videos/video_list.html', context)


def video_detail_view(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'videos/video_detail.html', {'video': video})


