from django.db import models

# Create your models here.


class MagazineDetails(models.Model):

    year = models.TextField(max_length=20)
    title = models.TextField(max_length=100)
    editor_name = models.TextField(max_length=1000)
    description = models.TextField(max_length=100000)
    document_link = models.TextField(max_length=10000)
    cover_image = models.ImageField(blank=True , upload_to='images')