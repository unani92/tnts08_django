from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Board(models.Model) : 
    name = models.CharField(max_length=10)
    title = models.CharField(max_length=30)
    choice = models.CharField(max_length=10)
    content = RichTextUploadingField(blank=True, null=True, config_name='special')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    