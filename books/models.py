from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Page(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='pages')
    page_number = models.PositiveIntegerField()
    image = models.ImageField(upload_to='book_pages/')

    class Meta:
        ordering = ['page_number']
