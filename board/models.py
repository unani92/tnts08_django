from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Board(models.Model) : 
    title = models.CharField(max_length=30)
    content = RichTextUploadingField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self) : 
        return f'{self.title}, {self.content},{self.created_at},{self.updated_at}'