from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.files import File
from .models import Book, Page
from pdf2image import convert_from_path
from pathlib import Path
import os


@receiver(post_save, sender=Book)
def generate_book_pages(sender, instance, created, **kwargs):
    if created and instance.pdf_file:
        try:
            output_dir = Path(settings.MEDIA_ROOT) / \
                f'book_pages/book_{instance.id}'
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

            # ✅ Save thumbnail from first image
            if images:
                thumb_dir = Path(settings.MEDIA_ROOT) / 'thumbnails'
                thumb_dir.mkdir(parents=True, exist_ok=True)

                thumb_path = thumb_dir / f'book_{instance.id}_thumb.jpg'
                images[0].save(thumb_path, 'JPEG')

                # Re-open file as Django File
                with open(thumb_path, 'rb') as f:
                    django_file = File(f)
                    instance.thumbnail.save(
                        f'book_{instance.id}_thumb.jpg', django_file, save=True)

                print(f"✅ Thumbnail saved at {instance.thumbnail.url}")

        except Exception as e:
            print(f"❌ Error generating book pages or thumbnail: {e}")
