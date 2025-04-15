from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Video
from moviepy.editor import VideoFileClip
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from PIL import Image
import os
from io import BytesIO
import tempfile


@receiver(post_save, sender=Video)
def generate_video_thumbnail(sender, instance, created, **kwargs):
    if created and instance.video_file and not instance.thumbnail:
        try:
            # Load the video
            with VideoFileClip(instance.video_file.path) as clip:
                frame = clip.get_frame(1.0)  # Get frame at 1 second

                # Convert frame (numpy array) to PIL Image
                image = Image.fromarray(frame)

                # Save to temporary buffer
                buffer = BytesIO()
                image.save(buffer, format='JPEG')
                buffer.seek(0)

                # Save to Django storage
                file_name = f"video_thumbnails/{instance.slug}_thumb.jpg"
                saved_path = default_storage.save(
                    file_name, ContentFile(buffer.read()))

                # Attach to model
                instance.thumbnail = saved_path
                instance.save(update_fields=["thumbnail"])
                print(f"✅ Thumbnail generated for video: {instance.title}")

        except Exception as e:
            print(f"❌ Error generating thumbnail: {e}")
