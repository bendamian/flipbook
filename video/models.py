from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from multiselectfield import MultiSelectField


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('video_category', args=[self.slug])


AGE_GROUP_CHOICES = (
    ('under_10', 'Under 10'),
    ('10_13', '10–13'),
    ('13_16', '13–16'),
    ('over_16', 'Over 16'),
)


class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    video_file = models.FileField(upload_to='videos/')
    thumbnail = models.ImageField(
        upload_to='video_thumbnails/', blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    # Stores multiple selections
    age_groups = MultiSelectField(choices=AGE_GROUP_CHOICES, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('video_detail', args=[self.id])
