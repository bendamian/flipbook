from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Book, Page
from pdf2image import convert_from_path
from pathlib import Path
from django.core.files import File


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

            # Save first page as thumbnail after loop
            if images:
                thumb_path = Path(settings.MEDIA_ROOT) / \
                    f'thumbnails/book_{instance.id}_thumb.jpg'
                images[0].save(thumb_path, 'JPEG')
                with open(thumb_path, 'rb') as f:
                    instance.thumbnail.save(
                        f'book_{instance.id}_thumb.jpg', File(f), save=True)

        except Exception as e:
            print(f"❌ Error processing PDF: {e}")


