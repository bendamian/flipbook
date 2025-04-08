from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book, Page
from pdf2image import convert_from_path
from pathlib import Path
import os


@receiver(post_save, sender=Book)
def generate_book_pages(sender, instance, created, **kwargs):
    if created:
        output_dir = Path(f'media/book_pages/book_{instance.id}')
        output_dir.mkdir(parents=True, exist_ok=True)
        images = convert_from_path(instance.pdf_file.path)

        for i, img in enumerate(images):
            image_path = output_dir / f'page_{i + 1}.jpg'
            img.save(image_path, 'JPEG')
            Page.objects.create(
                book=instance,
                page_number=i + 1,
                image=f'book_pages/book_{instance.id}/page_{i + 1}.jpg'
            )
