from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', args=[self.slug])


class Book(models.Model):
    title = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255, blank=True, null=True)
    # Optional description of the product
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=255, blank=True, unique=True)
    pdf_file = models.FileField(upload_to='pdfs/')
    thumbnail = models.ImageField(
        upload_to='thumbnails/', blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # You can switch to slug later
        return reverse('book_flip', args=[self.id])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def clean(self):
        if not self.pdf_file.name.endswith('.pdf'):
            raise ValidationError("Only PDF files are allowed.")


class Page(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='pages')
    page_number = models.PositiveIntegerField()
    image = models.ImageField(upload_to='book_pages/')

    class Meta:
        ordering = ['page_number']
